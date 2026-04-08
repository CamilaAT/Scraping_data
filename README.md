# Scraping_data

Repositorio con dos tareas de extracción y análisis de datos.

---

## Task 1 — Web Scraping: UNMSM 2026-II

Web scraping de resultados de admisión de la Universidad Nacional Mayor de San Marcos (UNMSM) 2026-II.

### ¿Qué hace el proyecto?
Extrae automáticamente los resultados de admisión de todas las carreras disponibles en el portal de admisión de UNMSM y los consolida en un archivo Excel.

### Instalación de dependencias
pip install selenium pandas openpyxl webdriver-manager

### ¿Cómo ejecutar el script?
python scraper.py

### ¿Qué contiene el output?
El archivo `output/resultados_sanmarcos.xlsx` contiene las siguientes columnas:
- Codigo: Código del postulante
- Apellidos y Nombres: Nombre completo del postulante
- Escuela: Carrera a la que postula
- Puntaje: Puntaje obtenido en el examen
- Merito EP: Orden de mérito
- Observacion: Estado del postulante (Alcanzó vacante, Ausente, etc.)

---

## Task 2 — API REST: RAWG Video Games Database

Consumo de la API de RAWG para extraer, analizar y comparar datos de videojuegos.

### ¿Qué hace el proyecto?
Consulta la API de RAWG para explorar juegos, comparar plataformas y géneros, y exportar un ranking de los mejores juegos de todos los tiempos.

### Instalación de dependencias
pip install requests pandas

### Estructura
api/
├── tarea_rawg_api.ipynb
└── output/
└── top20_rawg.csv

### ¿Qué contiene el output?
El archivo `api/output/top20_rawg.csv` contiene el top 20 juegos de todos los tiempos con las columnas: name, rating, metacritic, release_date, main_genre.