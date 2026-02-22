import pandas as pd

# =========================
print("PARTE 1: CARGA Y EXPLORACION DE DATOS")
# =========================

ruta = "/home/alecc/Documentos/ModalidadVirtual - ModalidadVirtual.csv"
df = pd.read_csv(ruta)

print("\nPrimeras 5 filas:")
print(df.head())

print("\nUltimas 5 filas:")
print(df.tail())

print("\nResumen estadistico:")
print(df.describe())

print("\nInformacion del DataFrame:")
print(df.info())


# =========================
print("\nPARTE 2: LIMPIEZA DE DATOS")
# =========================

print("\nValores nulos por columna:")
print(df.isnull().sum())

# Eliminar filas con valores nulos
df = df.dropna()

# Rellenar valores faltantes con 0 (si quedaran)
df = df.fillna(0)

# Eliminar columna innecesaria (ejemplo: time)
if "time" in df.columns:
    df = df.drop(columns=["time"])

print("\nColumnas actuales:")
print(df.columns)


# =========================
print("\nPARTE 3: FILTRADO Y SELECCION DE DATOS")
# =========================

# Filtrar: edad > 21 y acepta = "Si"
filtro = df[(df["edad"] > 21) & (df["acepta"] == "Si")]

print("\nFiltrado (edad > 21 y acepta = Si):")
print(filtro)

# Seleccionar columnas especificas
nuevo_df = df[["carrera", "edad", "sexo"]]

print("\nNuevo DataFrame con columnas seleccionadas:")
print(nuevo_df.head())


# =========================
print("\nPARTE 4: OPERACIONES Y AGRUPACION")
# =========================

print("\nSuma de edades:")
print(df["edad"].sum())

print("\nMedia de edades:")
print(df["edad"].mean())

# Agrupar por carrera y calcular media de edad
grupo = df.groupby("carrera")["edad"].mean()

print("\nMedia de edad por carrera:")
print(grupo)

# Tabla pivote
tabla_pivote = pd.pivot_table(
    df,
    values="edad",
    index="carrera",
    columns="sexo",
    aggfunc="mean"
)

print("\nTabla pivote (Edad promedio por carrera y sexo):")
print(tabla_pivote)


# =========================
print("\nPARTE 5: MANIPULACION DE DATOS")
# =========================

df_ordenado = df.sort_values(by="edad", ascending=True)

print("\nDataFrame ordenado por edad:")
print(df_ordenado.head())


# =========================
print("\nPARTE 6: GUARDAR RESULTADOS")
# =========================

df.to_csv("/home/alecc/Documentos/ModalidadVirtual_modificado.csv", index=False)

print("\nArchivo guardado correctamente.")