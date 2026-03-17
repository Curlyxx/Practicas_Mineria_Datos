import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Ejercicio 1

# =========================================================
# 1. Cargar los datos
# =========================================================

ruta = "/home/alecc/Descargas/PublicidadVentas.csv"
df = pd.read_csv(ruta)

print("\nPrimeros datos del dataset:")
print(df.head())

# =========================================================
# 2. Preparar variables
# =========================================================

X = df[['Inversion']]   # variable independiente
y = df['Ventas']        # variable dependiente

# =========================================================
# 3. Crear y entrenar modelo
# =========================================================

modelo = LinearRegression()
modelo.fit(X, y)

# predicciones
y_pred = modelo.predict(X)

# =========================================================
# 4. Evaluar modelo
# =========================================================

mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

print("\nEvaluación del modelo")
print("MSE:", mse)
print("R²:", r2)

# coeficientes
pendiente = modelo.coef_[0]
intercepto = modelo.intercept_

print("\nEcuación del modelo:")
print(f"Ventas = {pendiente:.2f} * Inversion + {intercepto:.2f}")

# =========================================================
# 5. Función para estimar ventas
# =========================================================

def estimar_ventas():
    pred = modelo.predict(pd.DataFrame([[3.0]], columns=["Inversion"]))
    return pred

# ejemplo
print("\nEstimación de ventas para inversión de 3.0:")
print(estimar_ventas())

# =========================================================
# 6. Visualización
# =========================================================

plt.figure(figsize=(8,5))

plt.scatter(X, y, label="Datos reales")
plt.plot(X, y_pred, label="Regresión lineal")

plt.xlabel("Inversión en publicidad (miles de dólares)")
plt.ylabel("Unidades vendidas")
plt.title("Relación entre inversión en publicidad y ventas")

ecuacion = f"y = {pendiente:.2f}x + {intercepto:.2f}"
plt.text(df['Inversion'].min(), df['Ventas'].max(), ecuacion)

plt.legend()
plt.grid(True)

plt.show()















# Ejercicio 2

# ======================================================
# 1. Cargar los datos
# ======================================================

ruta = "/home/alecc/Descargas/EdadSeguros.csv"
df = pd.read_csv(ruta)

df.columns = df.columns.str.strip()

print("\nPrimeros datos del dataset:")  # limpia espacios en columnas
print(df.head())

# ======================================================
# 2. Verificar relación con gráfico inicial
# ======================================================

plt.scatter(df["Edad"], df["Costo"])
plt.xlabel("Edad")
plt.ylabel("Costo del seguro")
plt.title("Relación entre edad y costo del seguro")
plt.grid(True)
plt.show()

# ======================================================
# 3. Preparar datos para regresión
# ======================================================

X = df[["Edad"]]
y = df["Costo"]

modelo = LinearRegression()
modelo.fit(X, y)

y_pred = modelo.predict(X)

# ======================================================
# 4. Parámetros del modelo
# ======================================================

pendiente = modelo.coef_[0]
intercepto = modelo.intercept_

print("\nEcuación del modelo:")
print(f"Costo = {pendiente:.2f} * Edad + {intercepto:.2f}")

# ======================================================
# 5. Evaluación
# ======================================================

mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

print("\nMSE:", mse)
print("R²:", r2)

# ======================================================
# 6. Intervalos de confianza aproximados
# ======================================================

error = np.std(y - y_pred)

limite_superior = y_pred + 2*error
limite_inferior = y_pred - 2*error

# ======================================================
# 7. Visualización final
# ======================================================

plt.figure(figsize=(8,5))

plt.scatter(X, y, label="Datos reales")

plt.plot(X, y_pred, label="Regresión lineal")

plt.fill_between(df["Edad"],
                 limite_inferior,
                 limite_superior,
                 alpha=0.2,
                 label="Intervalo confianza")

plt.xlabel("Edad")
plt.ylabel("Costo del seguro")
plt.title("Modelo de regresión Edad vs Costo")

plt.legend()
plt.grid(True)

plt.show()

# ======================================================
# 8. Predicciones para edades clave
# ======================================================

edades = pd.DataFrame({"Edad":[30,40,50,60]})

predicciones = modelo.predict(edades)

tabla = pd.DataFrame({
    "Edad": edades["Edad"],
    "Costo_estimado": predicciones
})

print("\nPredicciones para edades clave:")
print(tabla)















# Ejercicio 3

# ======================================================
# 1. Cargar los datos
# ======================================================

ruta = "/home/alecc/Descargas/PracticaExamenes.csv"
df = pd.read_csv(ruta)

df.columns = df.columns.str.strip()

print("\nPrimeros datos del dataset:")
print(df.head())

# ======================================================
# 2. Preparar variables
# ======================================================

X = df[['horas']]
y = df['puntuacion']

# ======================================================
# 3. Crear modelo de regresión
# ======================================================

modelo = LinearRegression()
modelo.fit(X, y)

y_pred = modelo.predict(X)

# ======================================================
# 4. Ecuación de la recta
# ======================================================

pendiente = modelo.coef_[0]
intercepto = modelo.intercept_

print("\nEcuación del modelo:")
print(f"Puntuacion = {pendiente:.2f} * Horas + {intercepto:.2f}")

# ======================================================
# 5. Calcular R²
# ======================================================

r2 = r2_score(y, y_pred)

print("\nR²:", r2)

# ======================================================
# 6. Gráfica
# ======================================================

plt.scatter(X, y, label="Datos reales")

plt.plot(X, y_pred, label="Regresión lineal")

plt.xlabel("Horas de práctica")
plt.ylabel("Puntuación del examen")
plt.title("Relación entre horas de práctica y puntuación")

plt.legend()
plt.grid(True)

plt.show()

# ======================================================
# 7. Predicción
# ======================================================

def predecir_puntuacion():
    
    horas = float(input("\nIngrese horas de práctica: "))
    
    pred = modelo.predict(pd.DataFrame([[horas]], columns=["horas"]))
    
    print("Puntuación estimada:", pred[0])

predecir_puntuacion()