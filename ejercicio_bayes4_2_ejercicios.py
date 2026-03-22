import pandas as pd
import numpy as np

# Modelado
from sklearn.naive_bayes import MultinomialNB

# Métricas
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# División de datos
from sklearn.model_selection import train_test_split

# Preprocesamiento
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer

# =========================================
# Parte 1: Cargar datos
# =========================================
ruta = "/home/alecc/Descargas/amazon_cells_labelled.txt"

df = pd.read_csv(ruta, sep='\t', header=None, names=['texto', 'sentimiento'])

print("Primeros datos:")
print(df.head())

print("\nInformación general:")
print(df.info())

print("\nConteo de clases:")
print(df['sentimiento'].value_counts())

# =========================================
# Parte 2: Preparación de datos
# =========================================

# (aunque ya es 0 y 1, usamos LabelEncoder por práctica)
le = LabelEncoder()
df['sentimiento'] = le.fit_transform(df['sentimiento'])

# Vectorización (texto → números)
vectorizador = CountVectorizer(stop_words='english')
X = vectorizador.fit_transform(df['texto'])
y = df['sentimiento']

print("\nNúmero de palabras:", len(vectorizador.vocabulary_))

# =========================================
# Parte 3: División de datos
# =========================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================================
# Parte 4: Modelo
# =========================================
modelo = MultinomialNB()

# =========================================
# Parte 5: Entrenamiento
# =========================================
modelo.fit(X_train, y_train)

# =========================================
# Parte 6: Predicciones
# =========================================
y_pred = modelo.predict(X_test)

print("\nPredicciones (primeros 10):")
print(y_pred[:10])

# =========================================
# Parte 7: Evaluación
# =========================================
print("\nAccuracy:", accuracy_score(y_test, y_pred))

print("\nMatriz de confusión:")
print(confusion_matrix(y_test, y_pred))

print("\nReporte de clasificación:")
print(classification_report(y_test, y_pred))

# =========================================
# Parte 8: Prueba con nuevos textos
# =========================================
ejemplos = [
    "This product is amazing",
    "Worst phone ever",
    "Battery life is excellent",
    "I hate this device"
]

X_nuevo = vectorizador.transform(ejemplos)
pred = modelo.predict(X_nuevo)

print("\nNuevas predicciones:")
for texto, p in zip(ejemplos, pred):
    resultado = "Positivo" if p == 1 else "Negativo"
    print(f"{texto} --> {resultado}")