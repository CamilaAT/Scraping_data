from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import os

def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    return driver

def get_career_links(driver, base_url):
    driver.get(base_url)
    WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "a"))
    )
    links = driver.find_elements(By.TAG_NAME, "a")
    career_links = []
    for link in links:
        href = link.get_attribute("href")
        text = link.text.strip()
        if href and ".html" in href and href != base_url and text:
            career_links.append({"carrera": text, "url": href})
    return career_links

def scrape_career(driver, carrera, url):
    try:
        driver.get(url)
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "table"))
        )
        time.sleep(2)

        # Cambiar paginación a -1 (todos) via DataTables API
        driver.execute_script("""
            let tableId = $('table.dataTable').attr('id');
            $('#' + tableId).DataTable().page.len(-1).draw();
        """)
        time.sleep(5)

        rows_data = driver.execute_script("""
            let rows = document.querySelectorAll('table tbody tr');
            let data = [];
            rows.forEach(row => {
                let cells = row.querySelectorAll('td');
                if (cells.length === 0) return;
                let codigo = cells[0] ? cells[0].innerText.trim() : '';
                if (!codigo || isNaN(codigo)) return;
                data.push({
                    codigo:      codigo,
                    nombre:      cells[1] ? cells[1].innerText.trim() : '',
                    escuela:     cells[2] ? cells[2].innerText.trim() : '',
                    puntaje:     cells[3] ? (cells[3].getAttribute('data-score') || '') : '',
                    merito:      cells[4] ? (cells[4].getAttribute('data-merit') || '') : '',
                    observacion: cells[5] ? cells[5].innerText.trim() : ''
                });
            });
            return data;
        """)

        records = []
        for row in rows_data:
            records.append({
                "Codigo":              row["codigo"],
                "Apellidos y Nombres": row["nombre"],
                "Escuela":             row["escuela"],
                "Puntaje":             row["puntaje"],
                "Merito EP":           row["merito"],
                "Observacion":         row["observacion"]
            })
        return records

    except Exception as e:
        print(f"Error en {carrera}: {e}")
        return []

def save_to_excel(all_data, output_path):
    df = pd.DataFrame(all_data)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_excel(output_path, index=False)
    print(f"Archivo guardado: {output_path} — {len(df)} registros")

def main():
    BASE_URL = "https://admision.unmsm.edu.pe/Website20262/A/A.html"
    OUTPUT_PATH = "output/resultados_sanmarcos.xlsx"

    driver = init_driver()
    all_data = []

    try:
        career_links = get_career_links(driver, BASE_URL)
        print(f"{len(career_links)} carreras encontradas")

        for i, career in enumerate(career_links):
            print(f"[{i+1}/{len(career_links)}] {career['carrera']}")
            results = scrape_career(driver, career["carrera"], career["url"])
            all_data.extend(results)
            time.sleep(1)

    except Exception as e:
        print(f"Error general: {e}")
    finally:
        driver.quit()

    if all_data:
        save_to_excel(all_data, OUTPUT_PATH)
    else:
        print("No se encontraron datos")

if __name__ == "__main__":
    main()