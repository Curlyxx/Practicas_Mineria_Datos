import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from sklearn.preprocessing import StandardScaler

# ─────────────────────────────────────────────────────────────
#  Configuración visual global
# ─────────────────────────────────────────────────────────────
COLORS = ['#E63946', '#457B9D', '#2A9D8F', '#E9C46A']
plt.rcParams.update({
    'figure.facecolor': '#0D1117',
    'axes.facecolor':   '#161B22',
    'axes.edgecolor':   '#30363D',
    'axes.labelcolor':  '#C9D1D9',
    'xtick.color':      '#8B949E',
    'ytick.color':      '#8B949E',
    'text.color':       '#C9D1D9',
    'grid.color':       '#21262D',
    'grid.linestyle':   '--',
    'grid.alpha':       0.5,
})

def scatter_clusters(ax, X, labels, title, legend_labels=None):
    unique = np.unique(labels)
    for i, lbl in enumerate(unique):
        mask = labels == lbl
        name = legend_labels[i] if legend_labels else f'Cluster {lbl}'
        ax.scatter(X[mask, 0], X[mask, 1],
                   color=COLORS[i % len(COLORS)], s=120,
                   edgecolors='white', linewidths=0.6,
                   zorder=3, label=name)
    ax.set_title(title, fontsize=11, fontweight='bold', pad=8)
    ax.legend(fontsize=8, framealpha=0.3)
    ax.grid(True)

def styled_dendrogram(ax, Z, labels, title, cut_height=None):
    dendrogram(Z, ax=ax, labels=labels,
               color_threshold=cut_height if cut_height else 0,
               above_threshold_color='#8B949E',
               leaf_font_size=9)
    ax.set_title(title, fontsize=11, fontweight='bold', pad=8)
    ax.set_ylabel('Distancia', fontsize=9)
    if cut_height:
        ax.axhline(y=cut_height, color='#E63946', linestyle='--',
                   linewidth=1.4, label=f'Corte h={cut_height}')
        ax.legend(fontsize=8, framealpha=0.3)
    ax.grid(True, axis='y')

# ═══════════════════════════════════════════════════════════════
#  EJERCICIO 1 — Agrupación básica
# ═══════════════════════════════════════════════════════════════
def ejercicio1():
    X = np.array([[1,1],[2,1],[5,5],[6,5],[10,10],[11,10]])
    labels_pts = ['A','B','C','D','E','F']

    Z = linkage(X, method='ward')
    lbl3 = fcluster(Z, t=3, criterion='maxclust')
    lbl2 = fcluster(Z, t=2, criterion='maxclust')

    fig = plt.figure(figsize=(16, 9), facecolor='#0D1117')
    fig.suptitle('Ejercicio 1 — Agrupación Básica (Ward)', fontsize=14,
                 fontweight='bold', color='#C9D1D9', y=0.97)

    gs = gridspec.GridSpec(2, 3, figure=fig, hspace=0.45, wspace=0.35)

    # 1. Datos sin clusters
    ax0 = fig.add_subplot(gs[0, 0])
    ax0.scatter(X[:,0], X[:,1], color='#8B949E', s=120,
                edgecolors='white', linewidths=0.6, zorder=3)
    for i, txt in enumerate(labels_pts):
        ax0.annotate(txt, (X[i,0]+0.2, X[i,1]+0.2), fontsize=9,
                     color='#C9D1D9')
    ax0.set_title('Datos originales', fontsize=11, fontweight='bold', pad=8)
    ax0.grid(True)

    # 2. Dendrograma completo
    ax1 = fig.add_subplot(gs[0, 1:])
    styled_dendrogram(ax1, Z, labels_pts, 'Dendrograma completo')

    # 3. 3 clusters
    ax2 = fig.add_subplot(gs[1, 0])
    scatter_clusters(ax2, X, lbl3, '3 Clusters')
    for i, txt in enumerate(labels_pts):
        ax2.annotate(txt, (X[i,0]+0.2, X[i,1]+0.2), fontsize=8,
                     color='#C9D1D9')

    # 4. Dendrograma con corte para 3 clusters
    ax3 = fig.add_subplot(gs[1, 1])
    styled_dendrogram(ax3, Z, labels_pts, 'Corte → 3 clusters', cut_height=8)

    # 5. 2 clusters
    ax4 = fig.add_subplot(gs[1, 2])
    scatter_clusters(ax4, X, lbl2, '2 Clusters')
    for i, txt in enumerate(labels_pts):
        ax4.annotate(txt, (X[i,0]+0.2, X[i,1]+0.2), fontsize=8,
                     color='#C9D1D9')

    plt.show()


# ═══════════════════════════════════════════════════════════════
#  EJERCICIO 2 — Segmentación de clientes
# ═══════════════════════════════════════════════════════════════
def ejercicio2():
    X_raw = np.array([[20,100],[22,120],[23,140],
                      [45,700],[46,750],[48,720],
                      [60,1500],[62,1600]])
    ids = [f'C{i+1}' for i in range(len(X_raw))]

    # Escalar para que edad y gasto tengan igual peso
    scaler = StandardScaler()
    X = scaler.fit_transform(X_raw)

    Z = linkage(X, method='ward')
    lbl2 = fcluster(Z, t=2, criterion='maxclust')
    lbl3 = fcluster(Z, t=3, criterion='maxclust')

    nombres_3 = {1:'Jóvenes/bajo gasto', 2:'Adultos/gasto medio', 3:'Mayores/alto gasto'}
    leyenda2 = ['Segmento A', 'Segmento B']
    leyenda3 = [nombres_3[k] for k in sorted(nombres_3)]

    fig = plt.figure(figsize=(16, 9), facecolor='#0D1117')
    fig.suptitle('Ejercicio 2 — Segmentación de Clientes', fontsize=14,
                 fontweight='bold', color='#C9D1D9', y=0.97)

    gs = gridspec.GridSpec(2, 3, figure=fig, hspace=0.45, wspace=0.35)

    # Datos originales (escala real)
    ax0 = fig.add_subplot(gs[0, 0])
    ax0.scatter(X_raw[:,0], X_raw[:,1], color='#8B949E', s=120,
                edgecolors='white', linewidths=0.6, zorder=3)
    for i, txt in enumerate(ids):
        ax0.annotate(txt, (X_raw[i,0]+0.4, X_raw[i,1]+20), fontsize=8,
                     color='#C9D1D9')
    ax0.set_xlabel('Edad'); ax0.set_ylabel('Gasto mensual ($)')
    ax0.set_title('Datos originales', fontsize=11, fontweight='bold', pad=8)
    ax0.grid(True)

    # Dendrograma
    ax1 = fig.add_subplot(gs[0, 1:])
    styled_dendrogram(ax1, Z, ids, 'Dendrograma (datos escalados)')

    # 2 clusters (espacio real)
    ax2 = fig.add_subplot(gs[1, 0])
    scatter_clusters(ax2, X_raw, lbl2, '2 Clusters', leyenda2)
    ax2.set_xlabel('Edad'); ax2.set_ylabel('Gasto ($)')
    for i, txt in enumerate(ids):
        ax2.annotate(txt, (X_raw[i,0]+0.4, X_raw[i,1]+20), fontsize=8,
                     color='#C9D1D9')

    # Dendrograma corte 2
    ax3 = fig.add_subplot(gs[1, 1])
    styled_dendrogram(ax3, Z, ids, 'Corte → 2 clusters', cut_height=2.5)

    # 3 clusters
    ax4 = fig.add_subplot(gs[1, 2])
    scatter_clusters(ax4, X_raw, lbl3, '3 Clusters', leyenda3)
    ax4.set_xlabel('Edad'); ax4.set_ylabel('Gasto ($)')
    for i, txt in enumerate(ids):
        ax4.annotate(txt, (X_raw[i,0]+0.4, X_raw[i,1]+20), fontsize=8,
                     color='#C9D1D9')

    plt.show()


# ═══════════════════════════════════════════════════════════════
#  EJERCICIO 3 — Rendimiento académico
# ═══════════════════════════════════════════════════════════════
def ejercicio3():
    X = np.array([[95,98],[92,94],[88,90],
                  [65,70],[60,68],[58,62],
                  [30,40],[35,38]])
    alumnos = ['A','B','C','D','E','F','G','H']

    Z = linkage(X, method='ward')
    lbl2 = fcluster(Z, t=2, criterion='maxclust')
    lbl3 = fcluster(Z, t=3, criterion='maxclust')

    perfiles2 = ['Alto rendimiento', 'Bajo rendimiento']
    perfiles3 = ['Alto rendimiento', 'Rendimiento medio', 'Bajo rendimiento']

    fig = plt.figure(figsize=(16, 9), facecolor='#0D1117')
    fig.suptitle('Ejercicio 3 — Rendimiento Académico', fontsize=14,
                 fontweight='bold', color='#C9D1D9', y=0.97)

    gs = gridspec.GridSpec(2, 3, figure=fig, hspace=0.45, wspace=0.35)

    # Datos originales
    ax0 = fig.add_subplot(gs[0, 0])
    ax0.scatter(X[:,0], X[:,1], color='#8B949E', s=120,
                edgecolors='white', linewidths=0.6, zorder=3)
    for i, txt in enumerate(alumnos):
        ax0.annotate(txt, (X[i,0]+0.5, X[i,1]+0.5), fontsize=9,
                     color='#C9D1D9')
    ax0.set_xlabel('Promedio'); ax0.set_ylabel('Asistencia (%)')
    ax0.set_title('Datos originales', fontsize=11, fontweight='bold', pad=8)
    ax0.grid(True)

    # Dendrograma completo
    ax1 = fig.add_subplot(gs[0, 1:])
    styled_dendrogram(ax1, Z, alumnos, 'Dendrograma completo')

    # 2 clusters
    ax2 = fig.add_subplot(gs[1, 0])
    scatter_clusters(ax2, X, lbl2, '2 Clusters', perfiles2)
    ax2.set_xlabel('Promedio'); ax2.set_ylabel('Asistencia (%)')
    for i, txt in enumerate(alumnos):
        ax2.annotate(txt, (X[i,0]+0.5, X[i,1]+0.5), fontsize=8,
                     color='#C9D1D9')

    # Dendrograma corte 2 clusters
    ax3 = fig.add_subplot(gs[1, 1])
    styled_dendrogram(ax3, Z, alumnos, 'Corte → 2 clusters', cut_height=30)

    # 3 clusters
    ax4 = fig.add_subplot(gs[1, 2])
    scatter_clusters(ax4, X, lbl3, '3 Clusters', perfiles3)
    ax4.set_xlabel('Promedio'); ax4.set_ylabel('Asistencia (%)')
    for i, txt in enumerate(alumnos):
        ax4.annotate(txt, (X[i,0]+0.5, X[i,1]+0.5), fontsize=8,
                     color='#C9D1D9')

    plt.show()


# ═══════════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════════
if __name__ == '__main__':
    print("=" * 55)
    print("  CLUSTERING JERÁRQUICO — 3 Ejercicios")
    print("=" * 55)
    ejercicio1()
    ejercicio2()
    ejercicio3()
    print("\nTodos los ejercicios completados.")