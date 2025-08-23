import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from collections import Counter


def configurar_graficos():
    """Configuración general para los gráficos"""
    sns.set_style("whitegrid")
    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['axes.spines.right'] = False


def analizar_balance_clases(df, columna_objetivo='Churn'):
    """
    Analiza el balance de las clases en la variable objetivo
    """
    print("=" * 50)
    print(f'📊 ANÁLISIS DE BALANCE DE CLASES {columna_objetivo.upper()}')
    print("=" * 50)

    # Conteo de clases
    conteo_clases = df[columna_objetivo].value_counts()
    porcentaje_clases = df[columna_objetivo].value_counts(normalize=True) * 100

    print("\nConteo de clases:")
    for clase, conteo in conteo_clases.items():
        pct = porcentaje_clases[clase]
        print(f"{clase}: {conteo:,} ({pct:.2f}%)")

    # Visualización
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # Gráfico de barras
    conteo_clases.plot(kind='bar', ax=ax1, color=['#3498db', '#e74c3c'])
    ax1.set_title(f'Distribución de {columna_objetivo}', fontsize=14, fontweight='bold')
    ax1.set_xlabel(columna_objetivo)
    ax1.set_ylabel('Cantidad')
    ax1.tick_params(axis='x', rotation=0)

    # Agregar valores en las barras
    for i, v in enumerate(conteo_clases.values):
        ax1.text(i, v + 50, str(v), ha='center', va='bottom', fontweight='bold')

    # Gráfico de pastel
    ax2.pie(conteo_clases.values, labels=conteo_clases.index, autopct='%1.1f%%',
            colors=['#3498db', '#e74c3c'], startangle=90)
    ax2.set_title(f'Proporción de {columna_objetivo}', fontsize=14, fontweight='bold')

    plt.tight_layout()
    plt.show()

    return conteo_clases, porcentaje_clases