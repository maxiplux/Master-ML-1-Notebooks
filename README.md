# Aprendizaje Automático 1 — Notebooks (ICESI)

Este repositorio contiene los cuadernos (Jupyter Notebooks) y utilidades del curso "Aprendizaje Automático 1" de la Universidad ICESI. El objetivo es brindar una guía práctica y progresiva de conceptos de aprendizaje automático y estadística aplicada, desde regresión lineal (OLS) y sus supuestos, hasta clasificación y regularización, utilizando Python, JupyterLab y librerías estándar de ciencia de datos.

Fecha de última actualización: 2025-08-22 21:38 (hora local)

## Contenido del repositorio

- Notebooks principales (exploratorios y de práctica):
  - 0-SESION4-Practica-advertising.ipynb: práctica con un conjunto de datos de publicidad; regresión lineal y evaluación.
  - 1 - Sesion 3 Supuestos_teoricos.ipynb: revisión teórica de supuestos en modelos lineales.
  - 1- Sesion6-regresion_logistica(Sklearn).ipynb: regresión logística con scikit-learn.
  - 1-Churn_estudiante.ipynb: caso de churn (fuga de clientes) para práctica de clasificación.
  - 1-Sesión3 - OLS y gradient descent.ipynb: mínimos cuadrados ordinarios (OLS) y descenso por gradiente.
  - 1-sesion2-actividad (2).ipynb: actividad práctica de la sesión 2.
  - 1-statmodels_vs_sklearn.ipynb: comparación de regresión lineal con statsmodels vs. scikit-learn.
  - 1.0-Basic-Clasification.ipynb: conceptos básicos de clasificación.
  - 1_Sesion1-Correlación y Dependencia de Variables.ipynb: correlación y dependencia entre variables.
  - 2-SESION4-base_taller_futbol.ipynb y variante (1): análisis con base de taller de fútbol.
  - 2-Sesion4-multiple-polinomial.ipynb: regresión múltiple y polinomial.
  - 2_Sesion 1 - OLS.ipynb: fundamentos y práctica de OLS.
  - 3-actividad-regularizacion-estudiante.ipynb: actividad sobre regularización (p. ej., Ridge/Lasso).
  - 3_Sesion 1 - Supuestos_teoricos.ipynb: refuerzo de supuestos teóricos.
  - CRITICAL-FOR-DATA-ANALYTICS-1-Churn_solucion.ipynb: solución de referencia del caso de churn.
- Utilidades:
  - tools.py: funciones de apoyo para visualización y diagnóstico de balance de clases.
- Artefactos y datos:
  - data\: carpeta con archivos de datos utilizados por los notebooks.
  - Data-20250813 y Data-20250813.zip: instantáneas/paquetes de datos.
  - modelo_prestamo.pkl: modelo de ejemplo (pickle) para carga y evaluación.
  - reporte_exploratorio.html: reporte HTML de análisis exploratorio de datos (EDA).

## Requisitos

El entorno está basado en Python y Jupyter. Las dependencias se listan en el archivo `requeriments.txt` (observa que el nombre del archivo está intencionalmente escrito así en este repositorio).

Recomendado:
- Windows 10/11
- Python 3.11 (o 3.10/3.12 compatibles con las librerías listadas)
- JupyterLab o Jupyter Notebook

Principales librerías: numpy, pandas, matplotlib, seaborn, scikit-learn, statsmodels, scipy, jupyterlab/notebook y extensiones relacionadas (ver `requeriments.txt`).

## Instalación (Windows, PowerShell)

1) Clona o descarga este repositorio y ubica la ruta del proyecto:

```
C:\Users\franc\OneDrive\Documentos\AI\ICESI\Aprendizaje automatico 1\notebook\Notebooks - Sesion 1
```

2) Crea y activa un entorno virtual con Python 3.11 (recomendado):

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate
python -m pip install --upgrade pip
```

3) Instala las dependencias:

```powershell
pip install -r requeriments.txt
```

Si estás usando otra versión de Python instalada con el lanzador `py`, ajusta `-3.11` por la versión adecuada (por ejemplo, `-3.12`).

## Cómo ejecutar los notebooks

1) Con el entorno virtual activado, inicia Jupyter:

```powershell
jupyter lab
```

o bien:

```powershell
jupyter notebook
```

2) En el navegador, abre el notebook de interés dentro de la carpeta del proyecto. Por ejemplo, `1-Churn_estudiante.ipynb`.

3) Ejecuta las celdas en orden. Si un notebook depende de archivos de la carpeta `data\`, verifica que las rutas estén correctas y que los archivos existan.

## Utilidades incluidas (tools.py)

El archivo `tools.py` incluye funciones de apoyo para la visualización y el análisis del balance de clases.

- configurar_graficos(): define un estilo base para plots (seaborn whitegrid, oculta ejes superior/derecho).
- analizar_balance_clases(df, columna_objetivo='Churn'): imprime conteos y porcentajes por clase y muestra gráficos de barras y pastel; retorna conteo y porcentaje.

Ejemplo de uso dentro de un notebook:

```python
import pandas as pd
from tools import configurar_graficos, analizar_balance_clases

# Ejemplo mínimo de datos
df = pd.DataFrame({'Churn': ['Yes', 'No', 'No', 'Yes', 'No']})

configurar_graficos()
conteo, porcentaje = analizar_balance_clases(df, columna_objetivo='Churn')
```

## Datos y artefactos

- `data\`: coloca aquí los archivos CSV/Excel u otros usados por los notebooks. Ajusta las rutas según necesidad.
- `Data-20250813.zip`: paquete de datos. Si es necesario, descomprímelo para acceder a los archivos.
- `modelo_prestamo.pkl`: ejemplo de modelo serializado. Para cargarlo:

```python
import joblib
modelo = joblib.load('modelo_prestamo.pkl')
```

- `reporte_exploratorio.html`: abre este archivo en el navegador para ver un EDA ya generado.

## Sugerencias y buenas prácticas

- Usa un entorno virtual por proyecto para evitar conflictos de dependencias.
- Mantén `pip` actualizado: `python -m pip install --upgrade pip`.
- Guarda una copia de seguridad de tus datos si vas a modificar los notebooks.
- Cuando trabajes con rutas en Windows, usa `r'...ruta...'` o dobles barras `\\` en Python para evitar problemas de escape.

## Resolución de problemas (Windows)

- Error al compilar/instalar dependencias:
  - Ejecuta primero: `python -m pip install --upgrade pip setuptools wheel`.
  - Asegúrate de tener una versión de Python compatible (3.10–3.12 suele funcionar con las versiones listadas).
- Jupyter no abre en el navegador:
  - Ejecuta `jupyter lab --no-browser` y copia la URL en el navegador manualmente.
  - Verifica que el firewall no bloquee la conexión local.
- Conflictos de versiones:
  - Considera crear un entorno limpio nuevo y reinstalar con `pip install -r requeriments.txt`.

## Créditos y licencia

Material de uso educativo para la asignatura "Aprendizaje Automático 1" (Universidad ICESI). A menos que se indique lo contrario en archivos específicos, este repositorio se distribuye con fines académicos.

Si tienes comentarios, detectas errores o deseas proponer mejoras, por favor abre un issue o envía un pull request.
