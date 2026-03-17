# 1 Librerias
# 2 Exploración
# 3 Correlación
# 4 Gráfico
# 5 Parámetros m, b, x
# 6 Gráfico recta
# 7 Predicciones individuales
# 8 Error cuadrático medio
# 9 Encontrar m que muestre el Error
# 10 Gráficar Error
# 11 Predecir

# Ejercicio 2:
# 1 Librerias
# 2 Exploración
# 3 Preparacion de datos
# 4 Deducir entrenamiento 80%, prueba 20%
# 5 crear modelo
# 6 evaluacion modelo
# 7 metricas
# 8 graficas y visualización
# 9 predicciones a partir de lo que salga

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =========================================================
# 1. Cargar CSV y explorar datos
# =========================================================

ruta = "/home/alecc/Descargas/train.csv"
df = pd.read_csv(ruta)

print("\nShape del dataset:")
print(df.shape)

print("\nPrimeras filas:")
print(df.head())

print("\nEstadisticas de variables usadas:")
print(df[['GrLivArea','SalePrice']].describe())

print("\nValores nulos:")
print(df[['GrLivArea','SalePrice']].isnull().sum())

# ---------------------------------------------------------
# MATRIZ DE CORRELACION
# ---------------------------------------------------------

print("\nMatriz de correlacion:")
corr_matrix = df.corr(numeric_only=True)
print(corr_matrix)

print("\nCorrelacion especifica con SalePrice:")
print(corr_matrix['SalePrice'].sort_values(ascending=False).head(10))


# ---------------------------------------------------------
# HEATMAP DE CORRELACION
# ---------------------------------------------------------

plt.figure(figsize=(10,8))
plt.imshow(corr_matrix, cmap='coolwarm', interpolation='nearest')
plt.colorbar()
plt.title("Mapa de calor de correlaciones")

plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=90)
plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)

plt.tight_layout()
plt.show()

# ---------------------------------------------------------
# INTERPRETACION DE CORRELACION
# ---------------------------------------------------------

print("\nInterpretacion de correlacion:")
print("1  -> correlacion positiva perfecta")
print("0  -> no hay correlacion")
print("-1 -> correlacion negativa perfecta")

corr_value = corr_matrix.loc['GrLivArea','SalePrice']
print("\nCorrelacion entre GrLivArea y SalePrice:", corr_value)


# =========================================================
# 2. Definir modelo lineal
# SalePrice = w * GrLivArea + b
# =========================================================

x = df['GrLivArea'].values
y = df['SalePrice'].values


# =========================================================
# 3. Graficar datos reales + recta inicial
# =========================================================

w = 125
b = 0

y_pred = w * x + b

plt.scatter(x, y, alpha=0.4, label="Datos reales")
plt.plot(x, y_pred, color="red", label="Modelo inicial")
plt.xlabel("GrLivArea")
plt.ylabel("SalePrice")
plt.title("Regresion lineal inicial")
plt.legend()
plt.show()


# =========================================================
# 4. Calcular predicciones y error cuadratico (MSE)
# =========================================================

def mse(y_real, y_pred):
    return np.mean((y_real - y_pred) ** 2)

error = mse(y, y_pred)

print("\nMSE inicial:", error)


# =========================================================
# 5. Crear grid de valores de w
# =========================================================

w_values = np.arange(50, 201, 1)


# =========================================================
# 6. Evaluar MSE para cada w
# =========================================================

def sum_error(w, x, y):
    b = 0
    y_pred = w * x + b
    return mse(y, y_pred)

errors = []

for w in w_values:
    err = sum_error(w, x, y)
    errors.append(err)


# =========================================================
# 7. Graficar curva error vs w
# =========================================================

plt.plot(w_values, errors)
plt.xlabel("w (pendiente)")
plt.ylabel("MSE")
plt.title("Error vs pendiente")
plt.show()


# =========================================================
# Encontrar el mejor w
# =========================================================

best_w = w_values[np.argmin(errors)]
best_error = min(errors)

print("\nMejor valor de w:", best_w)
print("Error minimo:", best_error)

