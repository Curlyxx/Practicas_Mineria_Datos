print("=== EJERCICIOS BÁSICOS EN PYTHON ===\n")

# 1️⃣ Par o impar
num = int(input("1) Ingresa un número: "))

if num % 2 == 0:
    print("Resultado: Par\n")
else:
    print("Resultado: Impar\n")


# 2️⃣ Positivo o negativo
num2 = float(input("2) Ingresa otro número: "))

if num2 > 0:
    print("Resultado: Positivo\n")
elif num2 < 0:
    print("Resultado: Negativo\n")
else:
    print("Resultado: Cero\n")


# 3️⃣ Mayor o menor de edad
edad = int(input("3) Ingresa tu edad: "))

if edad >= 18:
    print("Resultado: Mayor de edad\n")
else:
    print("Resultado: Menor de edad\n")


# 4️⃣ Aprobar o reprobar
calif = float(input("4) Ingresa tu calificación: "))

if calif >= 60:
    print("Resultado: Aprobado\n")
else:
    print("Resultado: Reprobado\n")


# 5️⃣ Calificación en letras
calif2 = int(input("5) Ingresa tu calificación numérica (0-100): "))

if calif2 >= 90:
    letra = "A"
elif calif2 >= 80:
    letra = "B"
elif calif2 >= 70:
    letra = "C"
elif calif2 >= 60:
    letra = "D"
else:
    letra = "F"

print("Resultado:", letra, "\n")


# 6️⃣ Estado del agua
temp = float(input("6) Ingresa temperatura en °C: "))

if temp < 0:
    estado = "Sólido"
elif temp <= 100:
    estado = "Líquido"
else:
    estado = "Vapor"

print("Resultado:", estado)

print("\n=== FIN ===")
