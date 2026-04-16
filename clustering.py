import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# =========================
# 1. Crear DataFrame
# =========================
data = {
    "Horas_estudio": [1, 2, 2, 3, 4, 5, 6, 7, 8, 9],
    "Calificacion":  [50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
}

df = pd.DataFrame(data)

# =========================
# 2. Convertir a array
# =========================
X = df[["Horas_estudio", "Calificacion"]].values

# =========================
# 3. Gráfica simple
# =========================
plt.figure()
plt.scatter(df["Horas_estudio"], df["Calificacion"])
plt.title("Datos originales")
plt.xlabel("Horas de estudio")
plt.ylabel("Calificación")
plt.show()

# =========================
# 4. Método del codo
# =========================
inercia = []
K_range = range(1, 6)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(X)
    inercia.append(kmeans.inertia_)

plt.figure()
plt.plot(K_range, inercia, marker='o')
plt.title("Método del codo")
plt.xlabel("Número de clusters (K)")
plt.ylabel("Inercia")
plt.show()

# =========================
# 5. Aplicar K-means (ejemplo con K=2)
# =========================
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(X)

labels = kmeans.labels_
centroides = kmeans.cluster_centers_

# =========================
# 6. Gráfica con clusters
# =========================
plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=labels)  # puntos agrupados
plt.scatter(centroides[:, 0], centroides[:, 1], marker='X', s=200)  # centroides

plt.title("Clustering con K-means")
plt.xlabel("Horas de estudio")
plt.ylabel("Calificación")

plt.show()