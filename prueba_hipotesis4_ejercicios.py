import numpy as np
from scipy import stats

# H₀: μ = 500 ml  (el contenido promedio es exactamente 500 ml)
# H₁: μ ≠ 500 ml  (el contenido promedio es diferente de 500 ml — prueba de dos colas)

# Datos de la muestra
botellas = np.array([498, 501, 499, 502, 500, 497, 503, 499, 501, 500])

# Prueba t de una muestra (dos colas, μ₀ = 500)
t_stat, p_value = stats.ttest_1samp(botellas, popmean=500)

print(f"t = {t_stat:.4f}")
print(f"p-value = {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print("Rechazar H₀")
else:
    print("No rechazar H₀")


# Ejercicio 2
# H₀: μ_música = μ_silencio  (no hay diferencia en las calificaciones entre grupos)
# H₁: μ_música ≠ μ_silencio  (existe diferencia en las calificaciones — prueba de dos colas)
print("=" * 30)

grupo_musica  = np.array([65, 70, 68, 72, 66, 69, 71, 67, 70, 68])
grupo_silencio = np.array([85, 88, 90, 87, 92, 86, 89, 91, 88, 90])

# Prueba de Welch (equal_var=False) — muestras independientes
t_stat, p_value = stats.ttest_ind(
    grupo_musica, grupo_silencio, equal_var=False
)

print(f"t = {t_stat:.4f}")
print(f"p-value = {p_value:.4f}")

alpha = 0.01
if p_value < alpha:
    print("Rechazar H₀")
else:
    print("No rechazar H₀")



# Ejercicio 3
# H₀: La distribución observada se ajusta a la distribución histórica esperada (40% / 35% / 25%)
# H₁: La distribución observada NO se ajusta a la distribución histórica
print("=" * 30)

# Frecuencias observadas este año
observados = np.array([200, 120, 80])   # Ing, Admin, Psico

# Proporciones y frecuencias esperadas
proporciones = np.array([0.40, 0.35, 0.25])
n = observados.sum()                   # n = 400
esperados = proporciones * n             # [160, 140, 100]

# Grados de libertad = k − 1 = 3 − 1 = 2
gl = len(observados) - 1

# Chi-cuadrada de bondad de ajuste
chi2_stat, p_value = stats.chisquare(
    f_obs=observados, f_exp=esperados
)

print(f"χ² = {chi2_stat:.4f}")
print(f"Grados de libertad = {gl}")
print(f"p-value = {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print("Rechazar H₀")
else:
    print("No rechazar H₀")