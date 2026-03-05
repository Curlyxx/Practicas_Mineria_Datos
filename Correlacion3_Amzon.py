import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

ruta = "/home/alecc/Documentos/Amazon Sale Report.csv"
df = pd.read_csv(ruta)

# ---------------------------------
# 1. Exploración del dataset
# ---------------------------------

print("\nPrimeras filas del dataset:")
print(df.head())

print("\nInformación general:")
print(df.info())

print("\nCantidad de valores nulos:")
print(df.isnull().sum())

print("\nDescripción estadística:")
print(df.describe())

# ---------------------------------
# 2. Limpieza básica
# ---------------------------------

# eliminar duplicados
df = df.drop_duplicates()

# eliminar filas donde falte el monto de venta
df = df.dropna(subset=["Amount"])

print("\nDataset después de limpieza:")
print(df.shape)

# ---------------------------------
# 3. Identificación del target
# ---------------------------------

target = "Amount"

print("\nVariable objetivo (target):", target)

# ---------------------------------
# 4. Identificación de variables numéricas
# ---------------------------------

numericas = df.select_dtypes(include=[np.number])

print("\nColumnas numéricas:")
print(numericas.columns)

# ---------------------------------
# 5. Matriz de correlación
# ---------------------------------

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

corr_matrix = numericas.corr()

print("\nMatriz de correlación:")
print(corr_matrix)

# ---------------------------------
# 6. Heatmap de correlaciones
# ---------------------------------

plt.figure(figsize=(10,6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Matriz de correlación")
plt.show()

# ---------------------------------
# 7. Correlación con el target
# ---------------------------------

print("\nCorrelación con el target (Amount):")

corr_target = corr_matrix[target].sort_values(ascending=False)

print(corr_target)

# ---------------------------------
# 8. Variables altamente correlacionadas con el target
# ---------------------------------

print("\nVariables con alta correlación con Amount:")

threshold = 0.5

for variable, valor in corr_target.items():
    
    if variable != target and abs(valor) > threshold:
        
        print(f"{variable} -> correlación: {valor}")

# ---------------------------------
# 9. Diagramas de dispersión contra el target
# ---------------------------------

for variable in numericas.columns:
    
    if variable != target:
        
        plt.figure()
        plt.scatter(df[variable], df[target])
        plt.xlabel(variable)
        plt.ylabel(target)
        plt.title(f"{variable} vs {target}")
        plt.show()