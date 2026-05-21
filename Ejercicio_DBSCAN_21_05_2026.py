import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

# ── 1. Crear el DataFrame ──────────────────────────────────────────────────────
ruta = "/home/alecc/Downloads/ejercicio_1_zonas_entrega.csv"

df = pd.read_csv(ruta)
print("── DataFrame ──────────────────────────────")
print(df.to_string(index=False))

# ── 2. Graficar los puntos sin clasificar ─────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle("Ejercicio 1 — Detección de Zonas de Entrega (DBSCAN)", fontsize=13, fontweight="bold")

ax1 = axes[0]
ax1.scatter(df["X"], df["Y"], color="steelblue", s=100, edgecolors="white", linewidths=0.8, zorder=3)
for _, row in df.iterrows():
    ax1.annotate(row["Punto"], (row["X"], row["Y"]), textcoords="offset points",
                 xytext=(6, 5), fontsize=8, color="#333")
ax1.set_title("Puntos sin clasificar", fontsize=11, fontweight="bold")
ax1.set_xlabel("X"); ax1.set_ylabel("Y")
ax1.grid(True, alpha=0.3, linestyle="--")
ax1.set_facecolor("#f8f8f8")

# ── 3. Aplicar DBSCAN ─────────────────────────────────────────────────────────
coords = df[["X", "Y"]].values
db = DBSCAN(eps=0.8, min_samples=3).fit(coords)

# ── 4. Agregar columna Cluster (-1 = ruido/outlier) ──────────────────────────
df["Cluster"] = db.labels_
print("\n── DataFrame con Clusters ─────────────────")
print(df.to_string(index=False))

# ── 5. Graficar clusters y resaltar outliers en negro ────────────────────────
palette = ["#E63946", "#2A9D8F", "#F4A261", "#457B9D", "#8338EC"]
ax2 = axes[1]

for label in sorted(set(db.labels_)):
    mask = df["Cluster"] == label
    subset = df[mask]
    if label == -1:
        ax2.scatter(subset["X"], subset["Y"], color="black", s=140,
                    marker="x", linewidths=2.5, zorder=5, label="Outlier (ruido)")
    else:
        ax2.scatter(subset["X"], subset["Y"], color=palette[label % len(palette)],
                    s=110, edgecolors="white", linewidths=0.8, zorder=3,
                    label=f"Zona {label + 1}")

for _, row in df.iterrows():
    ax2.annotate(row["Punto"], (row["X"], row["Y"]), textcoords="offset points",
                 xytext=(6, 5), fontsize=8, color="#333")

n_clusters = len(set(db.labels_)) - (1 if -1 in db.labels_ else 0)
n_outliers  = list(db.labels_).count(-1)

ax2.set_title(f"Clusters DBSCAN — Zonas: {n_clusters}  |  Outliers: {n_outliers}",
              fontsize=11, fontweight="bold")
ax2.set_xlabel("X"); ax2.set_ylabel("Y")
ax2.legend(fontsize=9, framealpha=0.85)
ax2.grid(True, alpha=0.3, linestyle="--")
ax2.set_facecolor("#f8f8f8")

plt.tight_layout()
plt.show()

    
    



















    

### Ejericio 2  
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from sklearn.cluster import DBSCAN, KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

# ── 1. Cargar el DataFrame ────────────────────────────────────────────────────
ruta = "/home/alecc/Downloads/ejercicio_2_sensores_ambientales.csv"

df = pd.read_csv(ruta)
df = df.rename(columns={"Temperatura_C": "Temperatura", "Humedad_pct": "Humedad"})
print("── 1. DataFrame ───────────────────────────────────────────────────────")
print(df.to_string(index=False))

# ── 2. Escalar con StandardScaler ─────────────────────────────────────────────
scaler  = StandardScaler()
X_scaled = scaler.fit_transform(df[["Temperatura", "Humedad"]])
print("\n── 2. Datos escalados (primeras 5 filas) ──────────────────────────────")
print(pd.DataFrame(X_scaled, columns=["Temp_scaled","Hum_scaled"]).head().to_string(index=False))

# ── 3. Gráfico k-distancia (k=3) para elegir eps ─────────────────────────────
k = 3
nbrs = NearestNeighbors(n_neighbors=k).fit(X_scaled)
distancias, _ = nbrs.kneighbors(X_scaled)
k_dist = np.sort(distancias[:, k - 1])[::-1]   # distancia al k-ésimo vecino, ordenada desc.

# ── 4. Aplicar DBSCAN y agregar columna Cluster ───────────────────────────────
EPS        = 0.7   # valor elegido a partir del codo del k-distance plot
MIN_SAMPLES = 3
db = DBSCAN(eps=EPS, min_samples=MIN_SAMPLES).fit(X_scaled)
df["Cluster"] = db.labels_

n_clusters = len(set(db.labels_)) - (1 if -1 in db.labels_ else 0)
n_outliers  = list(db.labels_).count(-1)

print("\n── 4. DataFrame con Clusters ──────────────────────────────────────────")
print(df.to_string(index=False))
print(f"\nClusters detectados : {n_clusters}")
print(f"Anomalías (Cluster=-1): {n_outliers}")
print("Sensores anómalos   :", df[df["Cluster"] == -1]["Sensor"].tolist())

# ── 5. Visualización: k-dist + DBSCAN + K-Means ───────────────────────────────
palette = ["#E63946", "#2A9D8F", "#F4A261", "#457B9D", "#8338EC"]
fig = plt.figure(figsize=(16, 12))
fig.suptitle("Ejercicio 2 — Segmentación de Sensores Ambientales",
             fontsize=14, fontweight="bold", y=1.01)
gs = gridspec.GridSpec(2, 2, figure=fig, hspace=0.38, wspace=0.32)

# -- Panel A: k-distancia ------
ax_k = fig.add_subplot(gs[0, 0])
ax_k.plot(range(len(k_dist)), k_dist, color="#E63946", linewidth=2)
ax_k.axhline(y=EPS, color="#457B9D", linestyle="--", linewidth=1.5,
             label=f"eps elegido = {EPS}")
ax_k.set_title(f"Gráfico k-distancia  (k={k})", fontsize=11, fontweight="bold")
ax_k.set_xlabel("Puntos ordenados (mayor → menor distancia)")
ax_k.set_ylabel(f"Distancia al {k}.° vecino más cercano")
ax_k.legend(fontsize=9)
ax_k.grid(True, alpha=0.3, linestyle="--")
ax_k.set_facecolor("#f8f8f8")

# -- Panel B: DBSCAN clusters (espacio original) ------
ax_db = fig.add_subplot(gs[0, 1])
for label in sorted(set(db.labels_)):
    mask = df["Cluster"] == label
    sub  = df[mask]
    if label == -1:
        ax_db.scatter(sub["Temperatura"], sub["Humedad"],
                      color="black", s=160, marker="X", zorder=5, label="Anomalía")
    else:
        ax_db.scatter(sub["Temperatura"], sub["Humedad"],
                      color=palette[label % len(palette)], s=100,
                      edgecolors="white", linewidths=0.7, zorder=3,
                      label=f"Grupo {label+1}")
for _, row in df.iterrows():
    ax_db.annotate(row["Sensor"], (row["Temperatura"], row["Humedad"]),
                   textcoords="offset points", xytext=(5, 4), fontsize=7, color="#333")
ax_db.set_title(f"DBSCAN  (eps={EPS}, min_samples={MIN_SAMPLES})\n"
                f"Grupos: {n_clusters}  |  Anomalías: {n_outliers}",
                fontsize=11, fontweight="bold")
ax_db.set_xlabel("Temperatura (°C)"); ax_db.set_ylabel("Humedad (%)")
ax_db.legend(fontsize=8, framealpha=0.85)
ax_db.grid(True, alpha=0.3, linestyle="--")
ax_db.set_facecolor("#f8f8f8")

# -- Panel C: DBSCAN en espacio escalado ------
ax_sc = fig.add_subplot(gs[1, 0])
for label in sorted(set(db.labels_)):
    mask = df["Cluster"] == label
    pts  = X_scaled[mask]
    if label == -1:
        ax_sc.scatter(pts[:, 0], pts[:, 1],
                      color="black", s=160, marker="X", zorder=5, label="Anomalía")
    else:
        ax_sc.scatter(pts[:, 0], pts[:, 1],
                      color=palette[label % len(palette)], s=100,
                      edgecolors="white", linewidths=0.7, zorder=3,
                      label=f"Grupo {label+1}")
ax_sc.set_title("DBSCAN — espacio escalado (StandardScaler)", fontsize=11, fontweight="bold")
ax_sc.set_xlabel("Temperatura (z-score)"); ax_sc.set_ylabel("Humedad (z-score)")
ax_sc.legend(fontsize=8, framealpha=0.85)
ax_sc.grid(True, alpha=0.3, linestyle="--")
ax_sc.set_facecolor("#f8f8f8")

# -- Panel D: K-Means (mismo k=3) para comparar ------
ax_km = fig.add_subplot(gs[1, 1])
km = KMeans(n_clusters=3, random_state=42, n_init=10)
km_labels = km.fit_predict(X_scaled)
df["KMeans"] = km_labels

km_palette = ["#F4A261", "#2A9D8F", "#8338EC"]
for label in sorted(set(km_labels)):
    mask = df["KMeans"] == label
    sub  = df[mask]
    ax_km.scatter(sub["Temperatura"], sub["Humedad"],
                  color=km_palette[label % len(km_palette)], s=100,
                  edgecolors="white", linewidths=0.7, zorder=3, label=f"Grupo {label+1}")
# Marcar las anomalías reales con borde negro
anomalias = df[df["Cluster"] == -1]
ax_km.scatter(anomalias["Temperatura"], anomalias["Humedad"],
              facecolors="none", edgecolors="black", s=220,
              linewidths=2, zorder=5, label="Anomalía real (DBSCAN)")
for _, row in df.iterrows():
    ax_km.annotate(row["Sensor"], (row["Temperatura"], row["Humedad"]),
                   textcoords="offset points", xytext=(5, 4), fontsize=7, color="#333")
ax_km.set_title("K-Means (k=3) — ¿detecta anomalías?\n○ = anomalía real según DBSCAN",
                fontsize=11, fontweight="bold")
ax_km.set_xlabel("Temperatura (°C)"); ax_km.set_ylabel("Humedad (%)")
ax_km.legend(fontsize=8, framealpha=0.85)
ax_km.grid(True, alpha=0.3, linestyle="--")
ax_km.set_facecolor("#f8f8f8")

plt.savefig("sensores_ambientales_dbscan.png", dpi=150, bbox_inches="tight")
plt.show()























# ── 1. Cargar el DataFrame ────────────────────────────────────────────────────
ruta = "/home/alecc/Downloads/ejercicio_3_fraude_bancario.csv"

df = pd.read_csv(ruta)
print("── 1. DataFrame ───────────────────────────────────────────────────────")
print(df.to_string(index=False))

# ── 2. Escalar con StandardScaler ─────────────────────────────────────────────
scaler   = StandardScaler()
X_scaled = scaler.fit_transform(df[["Monto", "Hora"]])
print("\n── 2. Datos escalados (primeras 5 filas) ──────────────────────────────")
print(pd.DataFrame(X_scaled, columns=["Monto_scaled", "Hora_scaled"]).head().to_string(index=False))

# ── 3. Gráfico k-distancia para determinar eps ───────────────────────────────
k = 3
nbrs = NearestNeighbors(n_neighbors=k).fit(X_scaled)
distancias, _ = nbrs.kneighbors(X_scaled)
k_dist = np.sort(distancias[:, k - 1])[::-1]

# ── 4. Aplicar DBSCAN y etiquetar transacciones ──────────────────────────────
EPS         = 0.6
MIN_SAMPLES = 3
db = DBSCAN(eps=EPS, min_samples=MIN_SAMPLES).fit(X_scaled)
df["Cluster"] = db.labels_

# Cluster 0 = grupo más grande (normales) → el resto son sospechosos
conteo = df[df["Cluster"] != -1]["Cluster"].value_counts()
cluster_normal = conteo.idxmax()

def etiquetar(row):
    if row["Cluster"] == -1:
        return "Sospechosa"
    elif row["Cluster"] == cluster_normal:
        return "Normal"
    else:
        return "Sospechosa"

df["Etiqueta"] = df.apply(etiquetar, axis=1)

n_clusters  = len(set(db.labels_)) - (1 if -1 in db.labels_ else 0)
n_sospechosas = (df["Etiqueta"] == "Sospechosa").sum()

print("\n── 4. DataFrame etiquetado ────────────────────────────────────────────")
print(df.to_string(index=False))

# ── 5. Visualización ─────────────────────────────────────────────────────────
fig = plt.figure(figsize=(15, 10))
fig.suptitle("Ejercicio 3 — Análisis de Patrones de Fraude Bancario",
             fontsize=14, fontweight="bold")
gs = gridspec.GridSpec(2, 2, figure=fig, hspace=0.38, wspace=0.32)

palette_cluster = ["#2A9D8F", "#F4A261", "#457B9D", "#8338EC"]

# Panel A: k-distancia
ax_k = fig.add_subplot(gs[0, 0])
ax_k.plot(range(len(k_dist)), k_dist, color="#E63946", linewidth=2)
ax_k.axhline(y=EPS, color="#457B9D", linestyle="--", linewidth=1.5,
             label=f"eps elegido = {EPS}")
ax_k.set_title(f"Gráfico k-distancia  (k={k})", fontsize=11, fontweight="bold")
ax_k.set_xlabel("Puntos ordenados (mayor → menor distancia)")
ax_k.set_ylabel(f"Distancia al {k}.° vecino más cercano")
ax_k.legend(fontsize=9)
ax_k.grid(True, alpha=0.3, linestyle="--")
ax_k.set_facecolor("#f8f8f8")

# Panel B: DBSCAN por cluster en espacio original
ax_db = fig.add_subplot(gs[0, 1])
for label in sorted(set(db.labels_)):
    mask = df["Cluster"] == label
    sub  = df[mask]
    if label == -1:
        ax_db.scatter(sub["Monto"], sub["Hora"], color="black", s=160,
                      marker="X", zorder=5, label="Ruido (outlier)")
    else:
        ax_db.scatter(sub["Monto"], sub["Hora"],
                      color=palette_cluster[label % len(palette_cluster)],
                      s=100, edgecolors="white", linewidths=0.7, zorder=3,
                      label=f"Cluster {label}")
for _, row in df.iterrows():
    ax_db.annotate(row["Transaccion"], (row["Monto"], row["Hora"]),
                   textcoords="offset points", xytext=(5, 4), fontsize=7, color="#333")
ax_db.set_title(f"DBSCAN  (eps={EPS}, min_samples={MIN_SAMPLES})\n"
                f"Clusters: {n_clusters}  |  Outliers: {(db.labels_ == -1).sum()}",
                fontsize=11, fontweight="bold")
ax_db.set_xlabel("Monto ($)"); ax_db.set_ylabel("Hora del día")
ax_db.legend(fontsize=8, framealpha=0.85)
ax_db.grid(True, alpha=0.3, linestyle="--")
ax_db.set_facecolor("#f8f8f8")

# Panel C: Normal vs Sospechosa
ax_et = fig.add_subplot(gs[1, 0])
colores_etiqueta = {"Normal": "#2A9D8F", "Sospechosa": "#E63946"}
for etiqueta, color in colores_etiqueta.items():
    sub = df[df["Etiqueta"] == etiqueta]
    marker = "o" if etiqueta == "Normal" else "X"
    ax_et.scatter(sub["Monto"], sub["Hora"], color=color, s=110,
                  marker=marker, edgecolors="white", linewidths=0.7,
                  zorder=3, label=etiqueta)
for _, row in df.iterrows():
    ax_et.annotate(row["Transaccion"], (row["Monto"], row["Hora"]),
                   textcoords="offset points", xytext=(5, 4), fontsize=7, color="#333")
ax_et.set_title("Transacciones: Normales vs Sospechosas", fontsize=11, fontweight="bold")
ax_et.set_xlabel("Monto ($)"); ax_et.set_ylabel("Hora del día")
ax_et.legend(fontsize=9, framealpha=0.85)
ax_et.grid(True, alpha=0.3, linestyle="--")
ax_et.set_facecolor("#f8f8f8")

# Panel D: K-Means para comparación
ax_km = fig.add_subplot(gs[1, 1])
km = KMeans(n_clusters=2, random_state=42, n_init=10)
km_labels = km.fit_predict(X_scaled)
df["KMeans"] = km_labels
km_palette = ["#2A9D8F", "#F4A261"]
for label in sorted(set(km_labels)):
    sub = df[df["KMeans"] == label]
    ax_km.scatter(sub["Monto"], sub["Hora"],
                  color=km_palette[label], s=100,
                  edgecolors="white", linewidths=0.7, zorder=3, label=f"Grupo {label+1}")
sospechosas_reales = df[df["Etiqueta"] == "Sospechosa"]
ax_km.scatter(sospechosas_reales["Monto"], sospechosas_reales["Hora"],
              facecolors="none", edgecolors="black", s=220,
              linewidths=2, zorder=5, label="Sospechosa real (DBSCAN)")
for _, row in df.iterrows():
    ax_km.annotate(row["Transaccion"], (row["Monto"], row["Hora"]),
                   textcoords="offset points", xytext=(5, 4), fontsize=7, color="#333")
ax_km.set_title("K-Means (k=2) — comparación\n○ = sospechosa real según DBSCAN",
                fontsize=11, fontweight="bold")
ax_km.set_xlabel("Monto ($)"); ax_km.set_ylabel("Hora del día")
ax_km.legend(fontsize=8, framealpha=0.85)
ax_km.grid(True, alpha=0.3, linestyle="--")
ax_km.set_facecolor("#f8f8f8")

plt.savefig("fraude_bancario_dbscan.png", dpi=150, bbox_inches="tight")
plt.show()

# ── 6. Porcentaje de transacciones sospechosas ────────────────────────────────
pct = n_sospechosas / len(df) * 100
print(f"\n── 6. Porcentaje de transacciones sospechosas ─────────────────────────")
print(f"Sospechosas : {n_sospechosas} de {len(df)}  →  {pct:.1f}%")
print("Transacciones sospechosas:", df[df["Etiqueta"] == "Sospechosa"]["Transaccion"].tolist())
