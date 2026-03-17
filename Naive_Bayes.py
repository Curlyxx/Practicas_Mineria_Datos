import numpy as np
from sklearn.naive_bayes import BernoulliNB

# =========================================
# 1. Datos en texto (oraciones)
# =========================================

texto = """
mensaje,clase
"gana dinero gratis ahora",spam
"oferta especial solo hoy",spam
"reunion mañana en la oficina",nospam
"tarea de matematicas para mañana",nospam
"dinero gratis oferta limitada",spam
"""

# =========================================
# 2. Leer datos
# =========================================

lineas = texto.strip().split("\n")[1:]

mensajes = []
clases = []

for linea in lineas:
    partes = linea.split(",")
    mensaje = partes[0].replace('"', '')
    clase = partes[1]

    mensajes.append(mensaje)
    clases.append(1 if clase == "spam" else 0)

# =========================================
# 3. Crear vocabulario (palabras únicas)
# =========================================

vocabulario = set()

for mensaje in mensajes:
    for palabra in mensaje.split():
        vocabulario.add(palabra)

vocabulario = sorted(list(vocabulario))

print("Vocabulario:")
print(vocabulario)

# =========================================
# 4. Convertir a matriz 0 y 1
# =========================================

def vectorizar(mensaje):
    palabras = mensaje.split()
    return [1 if palabra in palabras else 0 for palabra in vocabulario]

X = np.array([vectorizar(m) for m in mensajes])
y = np.array(clases)

print("\nMatriz X:")
print(X)

print("\nClases y:")
print(y)

# =========================================
# 5. Entrenar modelo
# =========================================

modelo = BernoulliNB()
modelo.fit(X, y)

# =========================================
# 6. Probar con nuevo mensaje
# =========================================

nuevo_mensaje = "diner de tarea"
nuevo_vector = np.array([vectorizar(nuevo_mensaje)])

pred = modelo.predict(nuevo_vector)

print("\nMensaje nuevo:", nuevo_mensaje)
print("Predicción (1=spam, 0=no spam):", pred[0])