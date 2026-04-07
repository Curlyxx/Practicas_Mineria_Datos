import numpy as np
from scipy.stats import chi2_contingency

tabla = np.array([
    [85, 65],   # Ciudad A
    [50, 100]   # Ciudad B
])

chi2, p, dof, expected = chi2_contingency(tabla)
alpha = 0.05

print("=== EJERCICIO 1 ===")
print("Chi-cuadrada:", chi2)
print("p-value:", p)
print("Grados de libertad:", dof)
print("Frecuencias esperadas:\n", expected)

print("\n--- DECISIÓN ---")
if p < alpha:
    print("Se RECHAZA H0")
    print("Conclusión: Sí existe relación entre la ciudad y la preferencia de transporte.")
else:
    print("NO se rechaza H0")
    print("Conclusión: No hay evidencia suficiente de relación entre la ciudad y la preferencia de transporte.")





# Ejercicio 2

tabla = np.array([
    [40, 20],   # Sin estudios
    [35, 45],   # Bachillerato
    [15, 45]    # Universidad
])

chi2, p, dof, expected = chi2_contingency(tabla)
alpha = 0.05

print("\n=== EJERCICIO 2 ===")
print("Chi-cuadrada:", chi2)
print("p-value:", p)
print("Grados de libertad:", dof)
print("Frecuencias esperadas:\n", expected)

print("\n--- DECISIÓN ---")
if p < alpha:
    print("Se RECHAZA H0")
    print("Conclusión: Sí existe relación entre el nivel educativo y el hábito de fumar.")
else:
    print("NO se rechaza H0")
    print("Conclusión: No hay evidencia suficiente de relación entre el nivel educativo y el hábito de fumar.")



# Ejercicio 3
tabla = np.array([
    [10, 50],   # Vegana
    [30, 40],   # Mixta
    [45, 5]     # Carnívora
])

chi2, p, dof, expected = chi2_contingency(tabla)
alpha = 0.05

print("\n=== EJERCICIO 3 ===")
print("Chi-cuadrada:", chi2)
print("p-value:", p)
print("Grados de libertad:", dof)
print("Frecuencias esperadas:\n", expected)

print("\n--- DECISIÓN ---")
if p < alpha:
    print("Se RECHAZA H0")
    print("Conclusión: Sí existe relación entre el tipo de dieta y el nivel de colesterol.")
else:
    print("NO se rechaza H0")
    print("Conclusión: No hay evidencia suficiente de relación entre el tipo de dieta y el nivel de colesterol.")



