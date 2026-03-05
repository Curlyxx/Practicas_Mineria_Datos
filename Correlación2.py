import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ruta = "/home/alecc/Documentos/streaming_platform.csv"
df = pd.read_csv(ruta)

# Mostrar columnas
print(df.dtypes)

# Seleccionar variables numéricas
numericas = df.select_dtypes(include=[np.number])
print(numericas.columns)

# Pares de variables que sí existen
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