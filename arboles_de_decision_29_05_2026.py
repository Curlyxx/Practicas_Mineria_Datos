"""
╔══════════════════════════════════════════════════════════════════╗
║         ÁRBOLES DE DECISIÓN ID3 - EJERCICIOS PRÁCTICOS          ║
║   Ejercicio 1: Nivel de Estrés   |   Ejercicio 2: Diabetes       ║
╚══════════════════════════════════════════════════════════════════╝
"""

import math
from collections import Counter
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from sklearn.tree import DecisionTreeClassifier, plot_tree

# ─────────────────────────────────────────────────────────────────
#  UTILIDADES COMUNES
# ─────────────────────────────────────────────────────────────────

def entropia(clases: list) -> float:
    n = len(clases)
    if n == 0:
        return 0.0
    conteo = Counter(clases)
    return sum(-(c/n)*math.log2(c/n) for c in conteo.values())


def ganancia_informacion(datos: list[dict], atributo: str, objetivo: str) -> float:
    n = len(datos)
    clases_totales = [d[objetivo] for d in datos]
    ent_total = entropia(clases_totales)
    valores = set(d[atributo] for d in datos)
    ent_pond = sum(
        (len(sub := [d[objetivo] for d in datos if d[atributo] == v]) / n) * entropia(sub)
        for v in valores
    )
    return ent_total - ent_pond


def gini(clases: list) -> float:
    n = len(clases)
    if n == 0:
        return 0.0
    return 1.0 - sum((c/n)**2 for c in Counter(clases).values())


def ganancia_gini(datos: list[dict], atributo: str, objetivo: str) -> float:
    n = len(datos)
    gini_total = gini([d[objetivo] for d in datos])
    valores = set(d[atributo] for d in datos)
    gini_pond = sum(
        (len(sub := [d[objetivo] for d in datos if d[atributo] == v]) / n) * gini(sub)
        for v in valores
    )
    return gini_total - gini_pond


# ─────────────────────────────────────────────────────────────────
#  ÁRBOL ID3 GENÉRICO (implementación propia)
# ─────────────────────────────────────────────────────────────────

class NodoArbol:
    def __init__(self, atributo=None, hijos=None, clase=None):
        self.atributo = atributo
        self.hijos    = hijos or {}
        self.clase    = clase

    def es_hoja(self):
        return self.clase is not None


def construir_id3(datos: list[dict], atributos: list[str], objetivo: str) -> NodoArbol:
    clases = [d[objetivo] for d in datos]
    if len(set(clases)) == 1:
        return NodoArbol(clase=clases[0])
    if not atributos:
        return NodoArbol(clase=Counter(clases).most_common(1)[0][0])
    ganancias = {a: ganancia_informacion(datos, a, objetivo) for a in atributos}
    mejor = max(ganancias, key=ganancias.get)
    nodo = NodoArbol(atributo=mejor)
    for v in sorted(set(d[mejor] for d in datos)):
        sub = [d for d in datos if d[mejor] == v]
        nodo.hijos[v] = construir_id3(sub, [a for a in atributos if a != mejor], objetivo)
    return nodo


def construir_cart(datos: list[dict], atributos: list[str], objetivo: str) -> NodoArbol:
    clases = [d[objetivo] for d in datos]
    if len(set(clases)) == 1:
        return NodoArbol(clase=clases[0])
    if not atributos:
        return NodoArbol(clase=Counter(clases).most_common(1)[0][0])
    ginis = {a: ganancia_gini(datos, a, objetivo) for a in atributos}
    mejor = max(ginis, key=ginis.get)
    nodo = NodoArbol(atributo=mejor)
    for v in sorted(set(d[mejor] for d in datos)):
        sub = [d for d in datos if d[mejor] == v]
        nodo.hijos[v] = construir_cart(sub, [a for a in atributos if a != mejor], objetivo)
    return nodo


def predecir(nodo: NodoArbol, muestra: dict) -> str:
    if nodo.es_hoja():
        return nodo.clase
    v = muestra.get(nodo.atributo)
    return predecir(nodo.hijos[v], muestra) if v in nodo.hijos else "Desconocido"


# ─────────────────────────────────────────────────────────────────
#  VISUALIZACIÓN CON plot_tree DE SKLEARN (estilo por defecto)
# ─────────────────────────────────────────────────────────────────

def encode(datos: list[dict], atributos: list[str], objetivo: str):
    """Codifica variables categóricas a enteros para sklearn."""
    mapas = {a: {v: i for i, v in enumerate(sorted(set(d[a] for d in datos)))}
             for a in atributos}
    mapa_obj = {v: i for i, v in enumerate(sorted(set(d[objetivo] for d in datos)))}
    X = np.array([[mapas[a][d[a]] for a in atributos] for d in datos])
    y = np.array([mapa_obj[d[objetivo]] for d in datos])
    clases = [v for v, _ in sorted(mapa_obj.items(), key=lambda x: x[1])]
    return X, y, clases


def graficar_arbol(datos: list[dict], atributos: list[str], objetivo: str,
                   titulo: str, archivo: str, criterion: str = "entropy"):
    X, y, clases = encode(datos, atributos, objetivo)
    clf = DecisionTreeClassifier(criterion=criterion, random_state=42)
    clf.fit(X, y)

    n_hojas = clf.get_n_leaves()
    fig, ax = plt.subplots(figsize=(max(10, n_hojas * 2.2), 6))
    plot_tree(clf,
              feature_names=atributos,
              class_names=clases,
              filled=True,
              rounded=True,
              impurity=True,
              proportion=False,
              fontsize=9,
              ax=ax)
    ax.set_title(titulo, fontsize=12)
    plt.tight_layout()
    plt.savefig(archivo, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  ✔  Imagen guardada → {archivo}")


# ─────────────────────────────────────────────────────────────────
#  EJERCICIO 1 – NIVEL DE ESTRÉS
# ─────────────────────────────────────────────────────────────────

def ejercicio_1():
    banner = "═" * 66
    print(f"\n{banner}")
    print("  EJERCICIO 1: PREDICCIÓN DE ESTRÉS EN ESTUDIANTES")
    print(banner)

    dataset = [
        {"Sueño": "Poco",       "Ejercicio": "No", "Carga_Tareas": "Alta",   "Estrés": "Sí"},
        {"Sueño": "Poco",       "Ejercicio": "No", "Carga_Tareas": "Normal", "Estrés": "Sí"},
        {"Sueño": "Poco",       "Ejercicio": "Sí", "Carga_Tareas": "Alta",   "Estrés": "Sí"},
        {"Sueño": "Suficiente", "Ejercicio": "No", "Carga_Tareas": "Alta",   "Estrés": "Sí"},
        {"Sueño": "Suficiente", "Ejercicio": "Sí", "Carga_Tareas": "Normal", "Estrés": "No"},
        {"Sueño": "Suficiente", "Ejercicio": "Sí", "Carga_Tareas": "Alta",   "Estrés": "No"},
        {"Sueño": "Poco",       "Ejercicio": "Sí", "Carga_Tareas": "Normal", "Estrés": "No"},
        {"Sueño": "Suficiente", "Ejercicio": "No", "Carga_Tareas": "Normal", "Estrés": "No"},
    ]

    atributos = ["Sueño", "Ejercicio", "Carga_Tareas"]
    objetivo  = "Estrés"

    # ── PASO 1: Entropía total ──────────────────────────────────
    clases = [d[objetivo] for d in dataset]
    ent_total = entropia(clases)
    conteo = Counter(clases)
    n = len(clases)

    print(f"\n{'─'*50}")
    print("  PASO 1 ▸ ENTROPÍA TOTAL DEL CONJUNTO")
    print(f"{'─'*50}")
    print(f"  Clases: {dict(conteo)}   (n={n})")
    for cls, cnt in conteo.items():
        p = cnt/n
        print(f"  P({cls}) = {cnt}/{n} = {p:.4f}  →  -{p:.4f}·log₂({p:.4f}) = {-p*math.log2(p):.4f}")
    print(f"\n  ➜  Entropía total H = {ent_total:.4f} bits")

    # ── PASO 2: Ganancia de información ────────────────────────
    print(f"\n{'─'*50}")
    print("  PASO 2 ▸ GANANCIA DE INFORMACIÓN")
    print(f"{'─'*50}")

    ganancias = {}
    for attr in atributos:
        gi = ganancia_informacion(dataset, attr, objetivo)
        ganancias[attr] = gi
        for v in sorted(set(d[attr] for d in dataset)):
            sub = [d[objetivo] for d in dataset if d[attr] == v]
            print(f"    {attr}={v}: {Counter(sub)} → H={entropia(sub):.4f}  (n={len(sub)})")
        print(f"    ➜  Ganancia({attr}) = {gi:.4f}\n")

    # ── PASO 3: Nodo raíz ──────────────────────────────────────
    raiz = max(ganancias, key=ganancias.get)
    print(f"{'─'*50}")
    print("  PASO 3 ▸ SELECCIÓN DEL NODO RAÍZ")
    print(f"{'─'*50}")
    print(f"\n  {'Atributo':<18} {'Ganancia':>10}")
    print(f"  {'─'*30}")
    for attr in atributos:
        marca = " ◄ RAÍZ" if attr == raiz else ""
        print(f"  {attr:<18} {ganancias[attr]:>10.4f}{marca}")
    print(f"\n  ➜  Nodo raíz = [{raiz}]  (mayor ganancia)")

    # ── PASO 4: Árbol completo → imagen ───────────────────────
    print(f"\n{'─'*50}")
    print("  PASO 4 ▸ ÁRBOL DE DECISIÓN ID3 COMPLETO")
    print(f"{'─'*50}")
    construir_id3(dataset, atributos, objetivo)   # árbol propio (verificación)
    graficar_arbol(dataset, atributos, objetivo,
                   "Ejercicio 1 – Árbol ID3: Nivel de Estrés",
                   "arbol_estres.png",
                   criterion="entropy")

    # ── PASO 5: Predicción ────────────────────────────────────
    arbol = construir_id3(dataset, atributos, objetivo)
    muestra = {"Sueño": "Poco", "Ejercicio": "No", "Carga_Tareas": "Alta"}
    pred = predecir(arbol, muestra)
    print(f"\n{'─'*50}")
    print("  PASO 5 ▸ PREDICCIÓN")
    print(f"{'─'*50}")
    print(f"\n  Muestra: Sueño=Poco, Ejercicio=No, Carga_Tareas=Alta")
    print(f"\n  ➜  Predicción Estrés = [{pred}]")
    print(f"\n  Recorrido del árbol:")
    print(f"    [{raiz}?] → Poco → ...(continúa)... → Estrés={pred}")


# ─────────────────────────────────────────────────────────────────
#  EJERCICIO 2 – DIABETES
# ─────────────────────────────────────────────────────────────────

def ejercicio_2():
    banner = "═" * 66
    print(f"\n\n{banner}")
    print("  EJERCICIO 2: PREDICCIÓN DE DIABETES EN PACIENTES")
    print(banner)

    dataset = [
        {"IMC": "Alto",   "Azucar_Sangre": "Alta",   "Actividad_Fisica": "Poca",  "Diabetes": "Sí"},
        {"IMC": "Alto",   "Azucar_Sangre": "Alta",   "Actividad_Fisica": "Mucha", "Diabetes": "Sí"},
        {"IMC": "Alto",   "Azucar_Sangre": "Normal", "Actividad_Fisica": "Poca",  "Diabetes": "Sí"},
        {"IMC": "Normal", "Azucar_Sangre": "Alta",   "Actividad_Fisica": "Poca",  "Diabetes": "Sí"},
        {"IMC": "Normal", "Azucar_Sangre": "Normal", "Actividad_Fisica": "Mucha", "Diabetes": "No"},
        {"IMC": "Normal", "Azucar_Sangre": "Normal", "Actividad_Fisica": "Poca",  "Diabetes": "No"},
        {"IMC": "Alto",   "Azucar_Sangre": "Normal", "Actividad_Fisica": "Mucha", "Diabetes": "No"},
        {"IMC": "Normal", "Azucar_Sangre": "Alta",   "Actividad_Fisica": "Mucha", "Diabetes": "No"},
        {"IMC": "Normal", "Azucar_Sangre": "Normal", "Actividad_Fisica": "Poca",  "Diabetes": "No"},
        {"IMC": "Alto",   "Azucar_Sangre": "Alta",   "Actividad_Fisica": "Poca",  "Diabetes": "Sí"},
    ]

    atributos = ["IMC", "Azucar_Sangre", "Actividad_Fisica"]
    objetivo  = "Diabetes"

    # ── PASO 1: Entropía total ──────────────────────────────────
    clases = [d[objetivo] for d in dataset]
    ent_total  = entropia(clases)
    gini_total = gini(clases)
    conteo = Counter(clases)
    n = len(clases)

    print(f"\n{'─'*50}")
    print("  PASO 1 ▸ ENTROPÍA TOTAL DEL CONJUNTO")
    print(f"{'─'*50}")
    print(f"  Clases: {dict(conteo)}   (n={n})")
    for cls, cnt in conteo.items():
        p = cnt/n
        print(f"  P({cls}) = {cnt}/{n} = {p:.4f}  →  -{p:.4f}·log₂({p:.4f}) = {-p*math.log2(p):.4f}")
    print(f"\n  ➜  Entropía total H = {ent_total:.4f} bits")
    print(f"  ➜  Gini total       = {gini_total:.4f}")

    # ── PASO 2: Ganancia de información (ID3) ──────────────────
    print(f"\n{'─'*50}")
    print("  PASO 2 ▸ GANANCIA DE INFORMACIÓN (ID3 – Entropía)")
    print(f"{'─'*50}")

    ganancias_id3  = {}
    ganancias_gini = {}

    for attr in atributos:
        gi_id3  = ganancia_informacion(dataset, attr, objetivo)
        gi_gini = ganancia_gini(dataset, attr, objetivo)
        ganancias_id3[attr]  = gi_id3
        ganancias_gini[attr] = gi_gini

        for v in sorted(set(d[attr] for d in dataset)):
            sub = [d[objetivo] for d in dataset if d[attr] == v]
            print(f"    {attr}={v}: {Counter(sub)} → H={entropia(sub):.4f}  Gini={gini(sub):.4f}  (n={len(sub)})")
        print(f"    ➜  Ganancia ID3({attr})  = {gi_id3:.4f}")
        print(f"    ➜  Reducción Gini({attr}) = {gi_gini:.4f}\n")

    # ── PASO 3: Comparación ID3 vs CART ───────────────────────
    raiz_id3  = max(ganancias_id3,  key=ganancias_id3.get)
    raiz_gini = max(ganancias_gini, key=ganancias_gini.get)

    print(f"{'─'*50}")
    print("  PASO 3 ▸ COMPARACIÓN ID3 vs CART (GINI)")
    print(f"{'─'*50}")
    print(f"\n  {'Atributo':<20} {'Ganancia ID3':>14} {'Reduc. Gini':>14}")
    print(f"  {'─'*50}")
    for attr in atributos:
        m1 = " ◄" if attr == raiz_id3   else ""
        m2 = " ◄" if attr == raiz_gini  else ""
        print(f"  {attr:<20} {ganancias_id3[attr]:>14.4f}{m1:3}  {ganancias_gini[attr]:>10.4f}{m2}")
    print(f"\n  ➜  Raíz ID3  (entropía)  = [{raiz_id3}]")
    print(f"  ➜  Raíz CART (gini)      = [{raiz_gini}]")
    if raiz_id3 == raiz_gini:
        print(f"  ✔  Ambos criterios coinciden → mismo nodo raíz")
    else:
        print(f"  ✖  Los criterios difieren → árboles distintos")

    # ── PASO 4a: Árbol ID3 → imagen ────────────────────────────
    print(f"\n{'─'*50}")
    print("  PASO 4a ▸ ÁRBOL ID3 COMPLETO")
    print(f"{'─'*50}")
    graficar_arbol(dataset, atributos, objetivo,
                   "Ejercicio 2 – Árbol ID3 (Entropía): Diabetes",
                   "arbol_diabetes_id3.png",
                   criterion="entropy")

    # ── PASO 4b: Árbol CART → imagen ───────────────────────────
    print(f"\n{'─'*50}")
    print("  PASO 4b ▸ ÁRBOL CART (GINI) COMPLETO")
    print(f"{'─'*50}")
    graficar_arbol(dataset, atributos, objetivo,
                   "Ejercicio 2 – Árbol CART (Gini): Diabetes",
                   "arbol_diabetes_cart.png",
                   criterion="gini")

    # ── PASO 5: Predicción ────────────────────────────────────
    arbol_id3  = construir_id3 (dataset, atributos, objetivo)
    arbol_cart = construir_cart(dataset, atributos, objetivo)
    muestra = {"IMC": "Alto", "Azucar_Sangre": "Alta", "Actividad_Fisica": "Poca"}
    pred_id3  = predecir(arbol_id3,  muestra)
    pred_cart = predecir(arbol_cart, muestra)

    print(f"\n{'─'*50}")
    print("  PASO 5 ▸ PREDICCIÓN")
    print(f"{'─'*50}")
    print(f"\n  Muestra: IMC=Alto, Azucar_Sangre=Alta, Actividad_Fisica=Poca")
    print(f"\n  ➜  Predicción ID3  = [{pred_id3}]")
    print(f"  ➜  Predicción CART = [{pred_cart}]")
    if pred_id3 == pred_cart:
        print(f"  ✔  Ambos modelos concuerdan → Diabetes = {pred_id3}")
    else:
        print(f"  ⚠  Los modelos discrepan:")
        print(f"     ID3={pred_id3}  /  CART={pred_cart}")


# ─────────────────────────────────────────────────────────────────
#  PUNTO DE ENTRADA
# ─────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    ejercicio_1()
    ejercicio_2()
    print(f"\n{'═'*66}")
    print("  FIN DE LOS EJERCICIOS")
    print(f"{'═'*66}\n")