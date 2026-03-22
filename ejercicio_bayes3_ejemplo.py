import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# =========================================
# 1. Dataset más completo
# =========================================
data = {
    'fruta': ['Manzana','Manzana','Manzana','Naranja','Naranja','Naranja','Pera','Pera','Pera'],
    'color': ['Rojo','Rojo','Verde','Naranja','Naranja','Amarillo','Verde','Verde','Amarillo'],
    'peso': [150,160,140,180,170,175,130,135,140],
    'textura': ['Lisa','Lisa','Lisa','Rugosa','Rugosa','Rugosa','Lisa','Lisa','Lisa']
}

df = pd.DataFrame(data)
print("Dataset original:")
print(df)

# =========================================
# 2. Convertir datos categóricos a numéricos
# =========================================
le_color = LabelEncoder()
le_textura = LabelEncoder()
le_fruta = LabelEncoder()

df['color'] = le_color.fit_transform(df['color'])
df['textura'] = le_textura.fit_transform(df['textura'])
df['fruta'] = le_fruta.fit_transform(df['fruta'])

print("\nDataset numérico:")
print(df)

# =========================================
# 3. Variables (X = características, y = objetivo)
# =========================================
X = df[['color', 'peso', 'textura']]  # características
y = df['fruta']  # variable objetivo

# =========================================
# 4. División de datos (entrenamiento y prueba)
# =========================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# =========================================
# 5. Modelo Naive Bayes
# =========================================
modelo = GaussianNB()
modelo.fit(X_train, y_train)

# =========================================
# 6. Predicciones
# =========================================
y_pred = modelo.predict(X_test)

print("\nPredicciones:")
print(y_pred)

# =========================================
# 7. Evaluación
# =========================================
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nMatriz de confusión:")
print(confusion_matrix(y_test, y_pred))

# =========================================
# 8. Prueba con nueva fruta
# =========================================
# Ejemplo: color = Rojo, peso = 155, textura = Lisa
nuevo = [[le_color.transform(['Verde'])[0], 135, le_textura.transform(['Lisa'])[0]]]

pred = modelo.predict(nuevo)
fruta_predicha = le_fruta.inverse_transform(pred)

print("\nNueva predicción:", fruta_predicha[0])