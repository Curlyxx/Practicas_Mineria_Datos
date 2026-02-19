from ejercicio_estadistica import Estadistico

lista_numeros = [2,4,6,8,4,6,4]

estadistica = Estadistico(lista_numeros)



# estudiantes = {
#     "A001": {"nombre": "Ana", "edad": 20},
#     "A002": {"nombre": "Luis", "edad": 22},
#     "A003": {"nombre": "Carlos", "edad": 20},
#     "A004": {"nombre": "María", "edad": 21},
#     "A005": {"nombre": "Elena", "edad": 20},
# }

print("media", estadistica.media())
print("Mediana", estadistica.mediana())
print("Moda", estadistica.moda())




# # Extraer edades
# edades = [datos["edad"] for datos in estudiantes.values()]

# # Crear objeto
# estadistica = Estadistico(edades)

# # Llamar métodos
# print("Datos:", edades)
# print("Media:", estadistica.media())
# print("Mediana:", estadistica.mediana())
# print("Moda:", estadistica.moda())
