# Machine Learning 1 — Notebooks (ICESI)

This repository contains the Jupyter Notebooks and utilities for the "Machine Learning 1" course at Universidad ICESI. The objective is to provide a practical and progressive guide to machine learning concepts and applied statistics, from linear regression (OLS) and its assumptions to classification and regularization, using Python, JupyterLab, and standard data science libraries.

Last update: 2025-08-22 21:43 (local time)

## Repository Contents

- Main notebooks (exploratory and practice):
  - 0-SESION4-Practica-advertising.ipynb: practice with an advertising dataset; linear regression and evaluation.
  - 1 - Sesion 3 Supuestos_teoricos.ipynb: theoretical review of assumptions in linear models.
  - 1- Sesion6-regresion_logistica(Sklearn).ipynb: logistic regression with scikit-learn.
  - 1-Churn_estudiante.ipynb: customer churn case for classification practice.
  - 1-Sesión3 - OLS y gradient descent.ipynb: ordinary least squares (OLS) and gradient descent.
  - 1-sesion2-actividad (2).ipynb: practical activity from session 2.
  - 1-statmodels_vs_sklearn.ipynb: linear regression comparison between statsmodels vs. scikit-learn.
  - 1.0-Basic-Clasification.ipynb: basic classification concepts.
  - 1_Sesion1-Correlación y Dependencia de Variables.ipynb: correlation and dependence between variables.
  - 2-SESION4-base_taller_futbol.ipynb and variant (1): analysis with football workshop database.
  - 2-Sesion4-multiple-polinomial.ipynb: multiple and polynomial regression.
  - 2_Sesion 1 - OLS.ipynb: OLS fundamentals and practice.
  - 3-actividad-regularizacion-estudiante.ipynb: regularization activity (e.g., Ridge/Lasso).
  - 3_Sesion 1 - Supuestos_teoricos.ipynb: reinforcement of theoretical assumptions.
  - CRITICAL-FOR-DATA-ANALYTICS-1-Churn_solucion.ipynb: reference solution for the churn case.
- Utilities:
  - tools.py: support functions for visualization and class balance diagnostics.
- Artifacts and data:
  - data\: folder with data files used by the notebooks.
  - Data-20250813 and Data-20250813.zip: data snapshots/packages.
  - modelo_prestamo.pkl: example model (pickle) for loading and evaluation.
  - reporte_exploratorio.html: HTML report of exploratory data analysis (EDA).

## Requirements

The environment is based on Python and Jupyter. Dependencies are listed in the `requeriments.txt` file (note that the filename is intentionally spelled this way in this repository).

Recommended:
- Windows 10/11
- Python 3.11 (or 3.10/3.12 compatible with the listed libraries)
- JupyterLab or Jupyter Notebook

Main libraries: numpy, pandas, matplotlib, seaborn, scikit-learn, statsmodels, scipy, jupyterlab/notebook and related extensions (see `requeriments.txt`).

## Installation (Windows, PowerShell)

1) Clone or download this repository and locate the project path:

```
C:\Users\franc\OneDrive\Documentos\AI\ICESI\Aprendizaje automatico 1\notebook\Notebooks - Sesion 1
```

2) Create and activate a virtual environment with Python 3.11 (recommended):

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate
python -m pip install --upgrade pip
```

3) Install dependencies:

```powershell
pip install -r requeriments.txt
```

If you're using another Python version installed with the `py` launcher, adjust `-3.11` to the appropriate version (for example, `-3.12`).

## How to run the notebooks

1) With the virtual environment activated, start Jupyter:

```powershell
jupyter lab
```

or alternatively:

```powershell
jupyter notebook
```

2) In the browser, open the notebook of interest within the project folder. For example, `1-Churn_estudiante.ipynb`.

3) Execute the cells in order. If a notebook depends on files from the `data\` folder, verify that the paths are correct and that the files exist.

## Included utilities (tools.py)

The `tools.py` file includes support functions for visualization and class balance analysis.

- configurar_graficos(): defines a base style for plots (seaborn whitegrid, hides top/right axes).
- analizar_balance_clases(df, columna_objetivo='Churn'): prints class counts and percentages and shows bar and pie charts; returns count and percentage.

Usage example within a notebook:

```python
import pandas as pd
from tools import configurar_graficos, analizar_balance_clases

# Minimal data example
df = pd.DataFrame({'Churn': ['Yes', 'No', 'No', 'Yes', 'No']})

configurar_graficos()
conteo, porcentaje = analizar_balance_clases(df, columna_objetivo='Churn')
```

## Data and artifacts

- `data\`: place CSV/Excel files or others used by the notebooks here. Adjust paths as needed.
- `Data-20250813.zip`: data package. If necessary, decompress it to access the files.
- `modelo_prestamo.pkl`: example of serialized model. To load it:

```python
import joblib
modelo = joblib.load('modelo_prestamo.pkl')
```

- `reporte_exploratorio.html`: open this file in the browser to view a pre-generated EDA.

## Suggestions and best practices

- Use a virtual environment per project to avoid dependency conflicts.
- Keep `pip` updated: `python -m pip install --upgrade pip`.
- Save a backup copy of your data if you're going to modify the notebooks.
- When working with paths in Windows, use `r'...path...'` or double backslashes `\\` in Python to avoid escape issues.

## Troubleshooting (Windows)

- Error compiling/installing dependencies:
  - Run first: `python -m pip install --upgrade pip setuptools wheel`.
  - Make sure you have a compatible Python version (3.10–3.12 usually works with the listed versions).
- Jupyter doesn't open in the browser:
  - Run `jupyter lab --no-browser` and copy the URL into the browser manually.
  - Verify that the firewall doesn't block the local connection.
- Version conflicts:
  - Consider creating a new clean environment and reinstalling with `pip install -r requeriments.txt`.

## Credits and license

Educational material for the "Machine Learning 1" course (Universidad ICESI). Unless otherwise indicated in specific files, this repository is distributed for academic purposes.

If you have comments, detect errors, or wish to propose improvements, please open an issue or send a pull request.