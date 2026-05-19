# =========================
# AGRUPAMIENTO DE CLIENTES
# =========================

# Importar librerías
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# -------------------------
# 1. Crear DataFrame
# -------------------------

compras = [1, 2, 1.5, 10, 12, 11, 4, 5, 6]
gasto = [2, 3, 2.5, 9, 11, 10, 5, 6, 7]

df = pd.DataFrame({
    'Compras': compras,
    'Gasto': gasto
})

print("DataFrame:")
print(df)

# -------------------------
# 2. Graficar los puntos
# -------------------------

plt.figure(figsize=(6,5))
plt.scatter(df['Compras'], df['Gasto'])

plt.title('Clientes')
plt.xlabel('Compras al mes')
plt.ylabel('Gasto mensual (cientos de pesos)')
plt.grid(True)

plt.show()

# -------------------------
# 3. Método del codo
# -------------------------

X = df[['Compras', 'Gasto']]

inercias = []

# Probar diferentes valores de k
K = range(1, 6)

for k in K:
    modelo = KMeans(n_clusters=k, random_state=42, n_init=10)
    modelo.fit(X)
    inercias.append(modelo.inertia_)

# Graficar método del codo
plt.figure(figsize=(6,5))
plt.plot(K, inercias, marker='o')

plt.title('Método del Codo')
plt.xlabel('Número de clusters (k)')
plt.ylabel('Inercia')

plt.grid(True)
plt.show()

# -------------------------
# 4. Aplicar K-Means
# -------------------------
# Según el codo, k = 3 funciona bien

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)

df['Cluster'] = kmeans.fit_predict(X)

print("\nDataFrame con clusters:")
print(df)

# -------------------------
# 5. Mostrar centroides
# -------------------------

centroides = kmeans.cluster_centers_

print("\nCentroides:")
print(centroides)

# -------------------------
# 6. Graficar clusters
# -------------------------

plt.figure(figsize=(7,6))

# Graficar puntos por cluster
plt.scatter(
    df['Compras'],
    df['Gasto'],
    c=df['Cluster'],
    cmap='viridis',
    s=100
)

# Graficar centroides
plt.scatter(
    centroides[:, 0],
    centroides[:, 1],
    color='red',
    marker='X',
    s=300,
    label='Centroides'
)

plt.title('Clusters de Clientes')
plt.xlabel('Compras al mes')
plt.ylabel('Gasto mensual (cientos de pesos)')

plt.legend()
plt.grid(True)

plt.show()
























# =========================
# AGRUPAMIENTO DE PERSONAS
# SEGÚN SALUD FÍSICA
# =========================

# -------------------------
# 1. Crear DataFrame
# -------------------------

ejercicio = [0.5, 1, 1.5, 6, 7, 8, 2, 3, 4]
condicion = [2, 3, 2.5, 8, 9, 10, 4, 5, 6]

df = pd.DataFrame({
    'Ejercicio': ejercicio,
    'Condicion': condicion
})

print("DataFrame:")
print(df)

# -------------------------
# 2. Visualizar los datos
# -------------------------

plt.figure(figsize=(6,5))

plt.scatter(
    df['Ejercicio'],
    df['Condicion'],
    s=100
)

plt.title('Condición Física de Personas')
plt.xlabel('Horas de ejercicio por semana')
plt.ylabel('Nivel de condición física')

plt.grid(True)
plt.show()

# -------------------------
# 3. Método del codo
# -------------------------

X = df[['Ejercicio', 'Condicion']]

inercias = []
K = range(1, 6)

for k in K:
    modelo = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    modelo.fit(X)
    inercias.append(modelo.inertia_)

# Graficar método del codo
plt.figure(figsize=(6,5))

plt.plot(K, inercias, marker='o')

plt.title('Método del Codo')
plt.xlabel('Número de clusters')
plt.ylabel('Inercia')

plt.grid(True)
plt.show()

# -------------------------
# 4. Aplicar K-Means
# -------------------------
# Según el método del codo:
# k = 3

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

df['Cluster'] = kmeans.fit_predict(X)

print("\nDataFrame con clusters:")
print(df)

# -------------------------
# 5. Obtener centroides
# -------------------------

centroides = kmeans.cluster_centers_

print("\nCentroides:")
print(centroides)

# -------------------------
# 6. Graficar resultados
# -------------------------

plt.figure(figsize=(7,6))

plt.scatter(
    df['Ejercicio'],
    df['Condicion'],
    c=df['Cluster'],
    cmap='viridis',
    s=120
)

# Centroides
plt.scatter(
    centroides[:, 0],
    centroides[:, 1],
    marker='X',
    s=300,
    color='red',
    label='Centroides'
)

plt.title('Clusters de Condición Física')
plt.xlabel('Horas de ejercicio por semana')
plt.ylabel('Nivel de condición física')

plt.legend()
plt.grid(True)

plt.show()

# -------------------------
# Interpretación
# -------------------------

print("\nInterpretación de clusters:")

print("""
Cluster 0:
Personas con poca actividad física
y baja condición física.

Cluster 1:
Personas con actividad moderada
y condición física media.

Cluster 2:
Personas muy activas con excelente
condición física.
""")















# =========================
# AGRUPAMIENTO DE PRODUCTOS
# SEGÚN VENTAS
# =========================

# -------------------------
# 1. Crear DataFrame
# -------------------------

ventas = [2, 3, 2.5, 15, 18, 20, 5, 6, 7]
ingresos = [3, 4, 3.5, 9, 10, 10, 5, 6, 7]

df = pd.DataFrame({
    'Ventas': ventas,
    'Ingresos': ingresos
})

print("DataFrame:")
print(df)

# -------------------------
# 2. Graficar los datos
# -------------------------

plt.figure(figsize=(6,5))

plt.scatter(
    df['Ventas'],
    df['Ingresos'],
    s=100
)

plt.title('Ventas e Ingresos de Productos')
plt.xlabel('Número de ventas mensuales')
plt.ylabel('Nivel de ingresos')

plt.grid(True)
plt.show()

# -------------------------
# 3. Aplicar K-Means
# -------------------------

X = df[['Ventas', 'Ingresos']]

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# -------------------------
# 4. Asignar clusters
# -------------------------

df['Cluster'] = kmeans.fit_predict(X)

print("\nDataFrame con clusters:")
print(df)

# -------------------------
# 5. Obtener centroides
# -------------------------

centroides = kmeans.cluster_centers_

print("\nCentroides:")
print(centroides)

# -------------------------
# 6. Visualizar clusters
# -------------------------

plt.figure(figsize=(7,6))

plt.scatter(
    df['Ventas'],
    df['Ingresos'],
    c=df['Cluster'],
    cmap='viridis',
    s=120
)

# Dibujar centroides
plt.scatter(
    centroides[:, 0],
    centroides[:, 1],
    marker='X',
    color='red',
    s=300,
    label='Centroides'
)

plt.title('Clusters de Productos')
plt.xlabel('Número de ventas mensuales')
plt.ylabel('Nivel de ingresos')

plt.legend()
plt.grid(True)

plt.show()

# -------------------------
# Interpretación
# -------------------------

print("\nInterpretación de clusters:")

print("""
Cluster 0:
Productos con bajas ventas
y bajos ingresos.

Cluster 1:
Productos con ventas medias
e ingresos moderados.

Cluster 2:
Productos altamente vendidos
y con altos ingresos.
""")