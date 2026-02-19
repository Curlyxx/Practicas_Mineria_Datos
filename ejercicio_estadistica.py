

class Estadistico:

    def __init__(self, datos):
        self.datos = datos

    # Media (promedio)
    def media(self):
        suma = 0
        for numero in self.datos:
            suma += numero
        return suma / len(self.datos)

    # def media(self):
    #     suma = sum(self.datos)
    #     cantidad = len(self.datos)
    #     return suma/cantidad

    # Mediana
    def mediana(self):
        datos_ordenados = sorted(self.datos)
        n = len(datos_ordenados)
        mitad = n // 2

        if n % 2 == 0:
            return (datos_ordenados[mitad - 1] + datos_ordenados[mitad]) / 2
        else:
            return datos_ordenados[mitad]

    # Moda
    def moda(self):
        frecuencias = {}

        # Contar frecuencia
        for numero in self.datos:
            if numero in frecuencias:
                frecuencias[numero] += 1
            else:
                frecuencias[numero] = 1

        # Obtener frecuencia máxima
        max_frecuencia = max(frecuencias.values())

        # Si todos aparecen una sola vez → no hay moda
        if max_frecuencia == 1:
            return "No hay moda"

        # Buscar todos los números con esa frecuencia
        modas = []
        for numero, frecuencia in frecuencias.items():
            if frecuencia == max_frecuencia:
                modas.append(numero)

        return modas



# =============================
# Diccionario con varios datos
# =============================
