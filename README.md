# Scraping_data

Web scraping de resultados de admisión de la Universidad Nacional Mayor de San Marcos (UNMSM) 2026-II.

## ¿Qué hace el proyecto?
Extrae automáticamente los resultados de admisión de todas las carreras disponibles en el portal de admisión de UNMSM y los consolida en un archivo Excel.

## Instalación de dependencias
```bash
pip install selenium pandas openpyxl webdriver-manager
```

## ¿Cómo ejecutar el script?
```bash
python scraper.py
```

## ¿Qué contiene el output?
El archivo `output/resultados_sanmarcos.xlsx` contiene las siguientes columnas:
- **Codigo**: Código del postulante
- **Apellidos y Nombres**: Nombre completo del postulante
- **Escuela**: Carrera a la que postula
- **Puntaje**: Puntaje obtenido en el examen
- **Merito EP**: Orden de mérito
- **Observacion**: Estado del postulante (Alcanzó vacante, Ausente, etc.)