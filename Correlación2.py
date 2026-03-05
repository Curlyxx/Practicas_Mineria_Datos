import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

ruta = "/home/alecc/Documentos/streaming_platform.csv"
df = pd.read_csv(ruta)

# -----------------------------
# 1. Mostrar tipos de datos
# -----------------------------
print("\nTipos de datos:")
print(df.dtypes)

# -----------------------------
# 2. Seleccionar variables numéricas
# -----------------------------
numericas = df.select_dtypes(include=[np.number])

print("\nColumnas numéricas:")
print(numericas.columns)

# -----------------------------
# 3. Matriz de correlación
# -----------------------------
print("\nMatriz de correlación:")
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
corr_matrix = numericas.corr()

print(corr_matrix)

# -----------------------------
# 4. Heatmap de correlaciones
# -----------------------------
plt.figure()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Matriz de correlación")
plt.show()

# -----------------------------
# 5. Detectar multicolinealidad
# -----------------------------
print("\nPosible multicolinealidad (|corr| > 0.8):")

threshold = 0.8

for i in range(len(corr_matrix.columns)):
    for j in range(i):
        corr_value = corr_matrix.iloc[i, j]
        
        if abs(corr_value) > threshold:
            col1 = corr_matrix.columns[i]
            col2 = corr_matrix.columns[j]
            
            print(f"{col1} y {col2} -> correlación: {corr_value}")

# -----------------------------
# 6. Diagramas de dispersión
# -----------------------------
pares = [
    ("age", "hours_watched_per_week"),
    ("hours_watched_per_week", "number_of_sessions"),
    ("days_since_last_login", "hours_watched_per_week")
]

for x, y in pares:

    correlacion = df[x].corr(df[y])

    print(f"\nCorrelación entre {x} y {y}: {correlacion}")

    plt.figure()
    plt.scatter(df[x], df[y])
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(f"{x} vs {y}")
    plt.show()