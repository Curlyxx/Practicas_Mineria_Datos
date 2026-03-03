# ============================================
# IMPORTAR LIBRERÍAS (UNA SOLA VEZ)
# ============================================

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ============================================
# CARGAR DATASET
# ============================================

ruta = "/home/alecc/Documentos/datos_estudiantes_decision.csv"
df = pd.read_csv(ruta)

print("Primeras filas:")
print(df.head())

print("\nInformación general:")
print(df.info())

print("\nEstadísticas descriptivas:")
print(df.describe())


# ============================================
# PARES DE VARIABLES
# ============================================

pares = [
    ("horas_estudio", "calificacion"),
    ("horas_sueno", "nivel_estres"),
    ("uso_redes", "calificacion")
]


# ============================================
# DETECCIÓN DE OUTLIERS (IQR)
# ============================================

def detectar_outliers(columna):
    Q1 = df[columna].quantile(0.25)
    Q3 = df[columna].quantile(0.75)
    IQR = Q3 - Q1
    
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    
    outliers = df[(df[columna] < limite_inferior) | (df[columna] > limite_superior)]
    
    print(f"Outliers en {columna}: {len(outliers)}")

print("\n===== OUTLIERS =====")
for col in ["horas_estudio", "calificacion", 
            "horas_sueno", "nivel_estres", 
            "uso_redes"]:
    detectar_outliers(col)


# ============================================
# CORRELACIONES
# ============================================

print("\n===== PEARSON =====")
for x, y in pares:
    r = df[[x, y]].corr(method="pearson").iloc[0,1]
    print(f"{x} vs {y} → r = {round(r,3)}")

print("\n===== SPEARMAN =====")
for x, y in pares:
    rho = df[[x, y]].corr(method="spearman").iloc[0,1]
    print(f"{x} vs {y} → rho = {round(rho,3)}")


# ============================================
# GRÁFICAS CON PEARSON
# ============================================

def grafica_pearson(x, y):
    r = df[[x, y]].corr(method="pearson").iloc[0,1]
    
    plt.figure()
    plt.scatter(df[x], df[y])
    
    # Línea de regresión lineal
    m, b = np.polyfit(df[x], df[y], 1)
    plt.plot(df[x], m*df[x] + b)
    
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(f"{x} vs {y} | Pearson r = {round(r,3)}")
    plt.show()

print("\n===== GRÁFICAS PEARSON =====")
for x, y in pares:
    grafica_pearson(x, y)


# ============================================
# GRÁFICAS CON SPEARMAN (MISMA LÍNEA VISUAL)
# ============================================

def grafica_spearman(x, y):
    rho = df[[x, y]].corr(method="spearman").iloc[0,1]
    
    plt.figure()
    plt.scatter(df[x], df[y])
    
    # MISMA línea lineal solo como referencia visual
    m, b = np.polyfit(df[x], df[y], 1)
    plt.plot(df[x], m*df[x] + b)
    
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(f"{x} vs {y} | Spearman rho = {round(rho,3)}")
    plt.show()

print("\n===== GRÁFICAS SPEARMAN =====")
for x, y in pares:
    grafica_spearman(x, y)

