# H0 Hipotesis nula, no existe relacion
# H1 Hipotesis alternativa, si existe relacion
# Métodos estadísticos
# T student (uno, dos, muestras)
# usar chi cuadrada


### Chi cuadrada ###

# 1. Prueba de independencia, Son dos variables categóricas independientes entre si?
# 2. Prueba de bondad de ajuste, Se ajustan los datos a una distribución esperada?
# 3. Prueba  de Homogeneidad, Provienen las muestras de la misma distribución poblacional?
# Fórmula, la misma de chatgpt,

import numpy as np
from scipy.stats import chi2_contingency

# Tabla de contingencia
tabla = np.array([
    [8, 2],
    [3, 7]
])

# Prueba chi-cuadrada
chi2, p, dof, expected = chi2_contingency(tabla)

# Nivel de significancia
alpha = 0.05

print("Chi-cuadrada:", chi2)
print("p-value:", p)
print("Grados de libertad:", dof)
print("Frecuencias esperadas:\n", expected)

print("\n--- DECISIÓN ---")

if p < alpha:
    print("Se RECHAZA H0")
    print("Conclusión: Sí existe relación entre el género y si le gusta el juego.")
else:
    print("NO se rechaza H0")
    print("Conclusión: No hay evidencia suficiente para decir que existe relación entre el género y si le gusta el juego.")




















