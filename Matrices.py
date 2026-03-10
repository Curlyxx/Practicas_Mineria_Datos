"""
Ejemplo de arreglos de 1D, 2D, 3D y N dimensiones en Python
"""

# print("============== ARREGLO 1D ==============")

# # 1D (vector)
# vector = [10, 20, 30, 40, 50]

# print("Vector:", vector)

# print("Primer elemento:", vector[0])
# print("Tercer elemento:", vector[2])

# print("Recorrido del vector:")
# for elemento in vector:
#     print(elemento)


# print("\n============== ARREGLO 2D ==============")

# # 2D (matriz)
# matriz = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print("Matriz completa:")
# print(matriz)

# print("Elemento fila 1 columna 2:", matriz[0][1])

# print("Recorrido de matriz:")
# for fila in matriz:
#     for elemento in fila:
#         print(elemento, end=" ")
#     print()


# print("\n============== ARREGLO 3D ==============")

# # 3D (lista de matrices)
# arreglo3D = [
#     [
#         [1, 2],
#         [3, 4]
#     ],
#     [
#         [5, 6],
#         [7, 8]
#     ]
# ]

# print("Arreglo 3D:", arreglo3D)

# print("Elemento [0][1][1]:", arreglo3D[0][1][1])

# print("Recorrido del arreglo 3D:")

# for matriz in arreglo3D:
#     for fila in matriz:
#         for elemento in fila:
#             print(elemento, end=" ")
#         print()
#     print()


# print("\n============== ARREGLO N DIMENSIONES (NUMPY) ==============")

# # usar numpy para N dimensiones
# import numpy as np

# # crear arreglo de 4 dimensiones
# arr4D = np.zeros((2, 3, 4, 5))

# print("Forma del arreglo:", arr4D.shape)

# print("Acceder a elemento [0][1][2][3]:")
# print(arr4D[0][1][2][3])


# print("\n============== CREAR DIMENSIONES DINAMICAMENTE ==============")

# dimensiones = (3, 3, 3)

# arrND = np.ones(dimensiones)

# print("Arreglo de dimensiones:", dimensiones)
# print(arrND)

# print("Shape:", arrND.shape)


# print("\n============== EJEMPLO PRACTICO ==============")

# # ejemplo de matriz de calificaciones
# calificaciones = [
#     [80, 90, 70],
#     [85, 88, 92],
#     [60, 75, 78]
# ]

# print("Calificaciones:")

# for fila in calificaciones:
#     for nota in fila:
#         print(nota, end=" ")
#     print()




#######################  Aquí empieza el ejercicio de classroom, lo de arriba era teoría   #####################
import numpy as np

# Ejercicio 1 Crear un array de 10 números aleatorios enteros entre 0 y 100
array1 = np.random.randint(0, 101, 10)
print("1) Array de 10 enteros aleatorios entre 0 y 100:")
print(array1)
print()

# Ejercicio 2 Crear un array de 5 números aleatorios decimales entre 0 y 1
array2 = np.random.rand(5)
print("2) Array de 5 decimales aleatorios entre 0 y 1:")
print(array2)
print()

# Ejercicio 3 Crear dos arrays de números aleatorios enteros de longitud 5 y concatenarlos
array3 = np.random.randint(0, 100, 5)
array4 = np.random.randint(0, 100, 5)
concatenado = np.concatenate((array3, array4))

print("3) Array 1:", array3)
print("   Array 2:", array4)
print("   Concatenación:", concatenado)
print()

# Ejercicio 4 Crear un array de 10 enteros aleatorios y separarlo en dos arrays de 5
array5 = np.random.randint(0, 100, 10)
split_arrays = np.split(array5, 2)

print("4) Array original:", array5)
print("   Primera mitad:", split_arrays[0])
print("   Segunda mitad:", split_arrays[1])
print()

# Ejercicio 5 Crear una matriz de 3x3 con decimales aleatorios entre 0 y 1
matriz = np.random.rand(3,3)

print("5) Matriz 3x3 de decimales aleatorios:")
print(matriz)
print()

# Ejercicio 6 Crear un array de 10 enteros aleatorios y seleccionar 3 al azar
array6 = np.random.randint(0, 100, 10)
seleccion = np.random.choice(array6, 3)

print("6) Array:", array6)
print("   3 elementos seleccionados al azar:", seleccion)
print()

# Ejercicio 7 Crear un array de 10 enteros entre 0 y 100 y calcular la media
array7 = np.random.randint(0, 101, 10)
media = np.mean(array7)

print("7) Array:", array7)
print("   Media:", media)
print()

