import numpy as np
from scipy import stats

alpha = 0.05

# =========================================
# 🧪 EJERCICIO 1: UNA MUESTRA vs VALOR
# =========================================
print("\n--- EJERCICIO 1 ---")

muestra1 = np.array([
    47, 50, 43, 46, 44, 48, 49, 42, 45, 47,
    46, 44, 43, 45, 48, 47, 46, 44, 45, 43,
    46, 47, 48, 44, 45
])

mu = 45

t_stat1, p_value1 = stats.ttest_1samp(muestra1, mu)

print("Media:", np.mean(muestra1))
print("t_stat:", t_stat1)
print("p_value:", p_value1)

if p_value1 < alpha:
    print("Se rechaza H0")
else:
    print("No se rechaza H0")


# =========================================
# 🧪 EJERCICIO 2: DOS GRUPOS INDEPENDIENTES
# =========================================
print("\n--- EJERCICIO 2 ---")

grupo_A = np.array([
    5, 6, 7, 5, 6, 8, 7, 6, 5, 7,
    6, 7, 5, 6, 7
])

grupo_B = np.array([
    8, 9, 7, 8, 9, 10, 8, 9, 7, 8,
    9, 10, 8, 9, 8
])

t_stat2, p_value2 = stats.ttest_ind(grupo_A, grupo_B)

print("Media Grupo A:", np.mean(grupo_A))
print("Media Grupo B:", np.mean(grupo_B))
print("t_stat:", t_stat2)
print("p_value:", p_value2)

if p_value2 < alpha:
    print("Se rechaza H0")
else:
    print("No se rechaza H0")


# =========================================
# 🧪 EJERCICIO 3: ANTES vs DESPUÉS (PAREADO)
# =========================================
print("\n--- EJERCICIO 3 ---")

antes = [200, 210, 195, 220, 205, 198, 202, 215, 210, 199]
despues = [192, 201, 187, 209, 196, 190, 193, 206, 201, 191]

t_stat3, p_value3 = stats.ttest_rel(antes, despues)

print("Media Antes:", np.mean(antes))
print("Media Después:", np.mean(despues))
print("t_stat:", t_stat3)
print("p_value:", p_value3)

if p_value3 < alpha:
    print("Se rechaza H0")
else:
    print("No se rechaza H0")