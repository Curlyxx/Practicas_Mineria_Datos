import pandas as pd

# Crear un DataFrame
datos = {
    "Nombre": ["Ana", "Luis", "Mario", "Juan"],
    "Edad": [20, 22, 19, 21],
    "Calificacion": [85, 90, 78, 88]
}

df = pd.DataFrame(datos)

print("Tabla completa:")
print(df)

print("\nPromedio de calificaciones:")
print(df["Calificacion"].mean())
