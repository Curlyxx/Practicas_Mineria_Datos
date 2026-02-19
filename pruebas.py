print("=== MINI GUÍA DE PYTHON ===\n")

# -------------------------
# VARIABLES
# -------------------------
print(">> VARIABLES")

nombre = "Alex"
edad = 25
altura = 1.75
es_estudiante = True

print("Nombre:", nombre)
print("Edad:", edad)
print("Altura:", altura)
print("¿Es estudiante?:", es_estudiante)
print("Tipo de nombre:", type(nombre))
print("Tipo de edad:", type(edad))
print()


# -------------------------
# OPERACIONES
# -------------------------
print(">> OPERACIONES")

a = 10
b = 3

print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("Potencia:", a ** b)
print()


# -------------------------
# STRINGS
# -------------------------
print(">> STRINGS")

texto = "Python es genial"

print(texto.upper())
print(texto.lower())
print("Longitud:", len(texto))
print()


# -------------------------
# LISTAS
# -------------------------
print(">> LISTAS")

frutas = ["manzana", "banana", "uva"]
print(frutas)

frutas.append("naranja")
print("Nueva lista:", frutas)
print()


# -------------------------
# DICCIONARIOS
# -------------------------
print(">> DICCIONARIOS")

persona = {
    "nombre": "Alex",
    "edad": 25,
    "ciudad": "CDMX"
}

print(persona)
print("Nombre:", persona["nombre"])
print()


# -------------------------
# CONDICIONALES (if / elif / else)
# -------------------------
print(">> CONDICIONALES CON ELIF")

calificacion = 85

if calificacion >= 90:
    print("Excelente")
elif calificacion >= 80:
    print("Muy bien")
elif calificacion >= 70:
    print("Aprobado")
else:
    print("Reprobado")

print()


# -------------------------
# MATCH CASE (Python 3.10+)
# -------------------------
print(">> MATCH CASE")

opcion = 2

match opcion:
    case 1:
        print("Opción 1: Crear archivo")
    case 2:
        print("Opción 2: Editar archivo")
    case 3:
        print("Opción 3: Eliminar archivo")
    case _:
        print("Opción no válida")

print()


# -------------------------
# LOOPS
# -------------------------
print(">> LOOPS")

for i in range(5):
    print("Iteración:", i)

print()

for i in range(2,22,2):
    print("Iteración:", i)

print()

# -------------------------
# FUNCIONES
# -------------------------
print(">> FUNCIONES")

def saludar(nombre):
    return f"Hola {nombre}"

print(saludar("Alex"))

print("\n=== FIN ===")


# Crear una clase
class Perro:
    
    # Constructor (se ejecuta al crear el objeto)
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    # Método
    def ladrar(self):
        print("Guau guau!")

# Crear objeto
mi_perro = Perro("Firulais", 3)

# Usar el objeto
print(mi_perro.nombre)
mi_perro.ladrar()
