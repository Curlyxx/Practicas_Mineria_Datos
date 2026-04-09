# Bondad de ajuste

# Métodos estadisticos
# T student:
#     - 1 muestra
#     - 2 muestras
#     - 3 independientes

# Chi cuadrada:
#     - 3 independientes
#     - 4 Bondad de ajuste
#     - 5 Homogeneidad


import numpy as np
from scipy.stats import chisquare

# Frecuencias observadas
observadas = np.array([70, 40, 30, 35, 25])

# Probabilidades teóricas
p = np.array([0.30, 0.25, 0.20, 0.15, 0.10])

# Tamaño de muestra
n = observadas.sum()

# Frecuencias esperadas
esperadas = n * p

# Nivel de significancia
alpha = 0.05

# Prueba chi-cuadrada
res = chisquare(f_obs=observadas, f_exp=esperadas)

# Resultados
chi2 = res.statistic
p_value = res.pvalue
gl = len(observadas) - 1

# -----------------------------
# IMPRESIÓN COMPLETA
# -----------------------------

print("=== FRECUENCIAS ===")
for i in range(len(observadas)):
    print(f"Categoría {i+1}: Observada = {observadas[i]}, Esperada = {esperadas[i]:.2f}")

print("\n=== RESULTADOS ===")
print(f"Chi-cuadrada: {chi2:.4f}")
print(f"Valor p: {p_value:.4f}")
print(f"Grados de libertad: {gl}")
print(f"Alpha: {alpha}")

# -----------------------------
# DECISIÓN DE HIPÓTESIS
# -----------------------------

print("\n=== DECISIÓN ===")

if p_value <= alpha:
    print("p-value <= alpha")
    print("Se RECHAZA H0")
    print("Conclusión: Los datos NO siguen la distribución esperada")
else:
    print("p-value > alpha")
    print("NO se rechaza H0")
    print("Conclusión: Los datos siguen la distribución esperada")