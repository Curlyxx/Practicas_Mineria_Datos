# ==============================
# Ejercicio 1: Suma de los primeros N números
# ==============================

# Se espera: un número entero positivo
# Ejemplo de entrada: 5
# (Se sumará 1+2+3+4+5)

N = int(input("Ingresa un número entero positivo (ej: 5): "))

suma = 0

for i in range(1, N + 1):
    suma += i

print("La suma de 1 hasta", N, "es:", suma)


# ==============================
# Ejercicio 2: Factorial
# ==============================

# Se espera: entero positivo
# Ejemplo: 5
# Resultado: 5! = 120

num = int(input("\nIngresa un entero positivo para factorial (ej: 5): "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("El factorial de", num, "es:", factorial)


# ==============================
# Ejercicio 3: Tabla de multiplicar
# ==============================

# Se espera: cualquier número entero
# Ejemplo: 7
# Mostrará la tabla del 7

n = int(input("\nNúmero para tabla de multiplicar (ej: 7): "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)


# ==============================
# Ejercicio 4: Promedio de notas
# ==============================

# Se esperan: notas positivas (0–10 por ejemplo)
# Para terminar, ingresar una nota negativa
# Ejemplo: 8, 9, 7, -1

suma = 0
contador = 0

for _ in range(100):  # límite de seguridad
    nota = float(input("\nIngresa nota (negativa para terminar): "))
    
    if nota < 0:
        break
    
    suma += nota
    contador += 1

if contador > 0:
    promedio = suma / contador
    print("Promedio:", promedio)
else:
    print("No se ingresaron notas")


# ==============================
# Ejercicio 5: Potencia
# ==============================

# Se espera:
# Base: número real
# Exponente: entero positivo
# Ejemplo: base=2, exponente=3 → 8

base = float(input("\nBase (ej: 2): "))
exp = int(input("Exponente entero positivo (ej: 3): "))

resultado = 1

for _ in range(exp):
    resultado *= base

print("Resultado:", resultado)


# ==============================
# Ejercicio 6: Suma de pares en un rango
# ==============================

# Se esperan dos enteros A y B
# Ejemplo: A=1, B=10
# Suma: 2+4+6+8+10

A = int(input("Valor A (inicio del rango, ej: 1): "))
B = int(input("Valor B (fin del rango, ej: 10): "))

suma = 0  # acumulador de la suma

print("\nNúmeros pares que se sumarán:")

for i in range(A, B + 1):
    if i % 2 == 0:  # verificar si es par
        print("Se suma:", i)  # mostrar número par
        suma += i  # sumar al total
        print("Suma parcial:", suma)  # mostrar suma parcial

print("\nSuma total de números pares:", suma)
