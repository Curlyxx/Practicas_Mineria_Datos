import numpy as np
import scipy.stats as stats
import pandas as pd

def prueba_hipotesis(nombre, mu_0, x_bar, s, n, alpha):
    # Estadístico t
    t = (x_bar - mu_0) / (s / np.sqrt(n))
    
    # Valor crítico (cola izquierda)
    t_critica = stats.t.ppf(alpha, df=n-1)
    
    # p-value
    p_value = stats.t.cdf(t, df=n-1)
    
    # Decisión
    decision = "Rechazar H0" if t < t_critica else "No rechazar H0"
    
    # Mostrar resultados
    print(f"\n=== {nombre} ===")
    print(f"t calculada: {t:.4f}")
    print(f"t crítica: {t_critica:.4f}")
    print(f"p-value: {p_value:.6f}")
    print(f"Decisión: {decision}")
    
    # DataFrame (opcional, más descriptivo)
    df = pd.DataFrame({
        'Parámetro': ['Media teórica', 'Media muestral', 'Desv. estándar', 'n', 't calculada', 't crítica', 'p-value', 'Conclusión'],
        'Valor': [mu_0, x_bar, s, n, t, t_critica, p_value, decision]
    })
    
    print(df)


# =========================
# Problema 1: Tornillos
# =========================
prueba_hipotesis(
    "Problema 1: Tornillos",
    mu_0=10,
    x_bar=9.7,
    s=0.5,
    n=49,
    alpha=0.01
)

# =========================
# Problema 2: Baterías
# =========================
prueba_hipotesis(
    "Problema 2: Baterías",
    mu_0=20,
    x_bar=18.5,
    s=2.5,
    n=30,
    alpha=0.05
)

# =========================
# Problema 3: Harina
# =========================
prueba_hipotesis(
    "Problema 3: Harina",
    mu_0=1000,
    x_bar=990,
    s=12,
    n=40,
    alpha=0.02
)