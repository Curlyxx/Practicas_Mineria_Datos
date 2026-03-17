from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# =========================================
# 1. Datos en texto
# =========================================

texto = """
reseña,clase
"el producto funciona excelente",satisfecho
"muy buena calidad",satisfecho
"el producto llegó dañado",insatisfecho
"muy mala calidad",insatisfecho
"excelente producto y calidad",satisfecho
"""

# =========================================
# 2. Leer datos
# =========================================

lineas = texto.strip().split("\n")[1:]

reseñas = []
clases = []

for linea in lineas:
    partes = linea.split(",")
    texto_limpio = partes[0].replace('"', '')
    clase = partes[1]

    reseñas.append(texto_limpio)
    clases.append(clase)

# =========================================
# 3. Vectorizar texto (automático)
# =========================================

vectorizador = CountVectorizer()
X = vectorizador.fit_transform(reseñas)

print("Vocabulario:")
print(vectorizador.get_feature_names_out())

# =========================================
# 4. Entrenar modelo
# =========================================

modelo = MultinomialNB()
modelo.fit(X, clases)

# =========================================
# 5. Clasificar nuevo texto
# =========================================

nuevo = ["producto mala calidad"]
X_nuevo = vectorizador.transform(nuevo)

pred = modelo.predict(X_nuevo)

print("\nTexto:", nuevo[0])
print("Clasificación:", pred[0])













# Ejercicio 2, Clasificación de noticias

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# =========================================
# 1. Datos
# =========================================

textos = [
    "equipo gana campeonato",
    "nuevo telefono inteligente",
    "jugador anota gol decisivo",
    "empresa lanza nueva computadora",
    "equipo gana torneo"
]

clases = [
    "deportes",
    "tecnologia",
    "deportes",
    "tecnologia",
    "deportes"
]

# =========================================
# 2. Convertir texto a matriz
# =========================================

vectorizador = CountVectorizer()
X = vectorizador.fit_transform(textos)

print("Vocabulario:")
print(vectorizador.get_feature_names_out())

# =========================================
# 3. Entrenar modelo
# =========================================

modelo = MultinomialNB()  # usa Laplace automáticamente
modelo.fit(X, clases)

# =========================================
# 4. Probar nuevo texto
# =========================================

nuevo = [" celular de empresa de inteligencia"]
X_nuevo = vectorizador.transform(nuevo)

pred = modelo.predict(X_nuevo)

print("\nTexto:", nuevo[0])
print("Clasificación:", pred[0])