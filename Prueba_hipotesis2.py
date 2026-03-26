import numpy as np
from scipy import stats

# Datos de la muestra (calificaciones)
muestra = np.array([70, 72, 78, 75, 80, 74, 77, 73, 76, 79])

# Parámetros de la prueba
mu = 75          # media hipotética
alpha = 0.05     # nivel de significancia

# Cálculos básicos
media_muestral = np.mean(muestra)
desv_std = np.std(muestra, ddof=1)
n = len(muestra)

# Prueba t de una muestra
t_stat, p_value = stats.ttest_1samp(muestra, mu)

# Resultados
print("Media muestral:", media_muestral)
print("Desviación estándar:", desv_std)
print("Tamaño de muestra:", n)
print("t_stat:", t_stat)
print("p_value:", p_value)
print("alpha:", alpha)

# Decisión
if p_value < alpha:
    print("Se rechaza la hipótesis nula (H0)")
else:
    print("No se rechaza la hipótesis nula (H0)")