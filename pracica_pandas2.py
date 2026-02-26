# Manipulación Avanzada de DataFrames con .loc .iloc y .query
# se usa .loc .iloc y .quey

# Funciones de agregación y groupby para analisis profundo
# para agregación se usa sum(), mean(), count()
# para groupby se usa para agrupas una o varias columnas

# ordenamiento de datos con .sort_values(), .sort_index()

# Merge, join y concatenacion de datos: técnicas avanzadas
# existe el merge, merge combina DataFrame basados en columnas comunes,
# concatenacion solo une, solo agrega

# Manejo de datos faltantes y técnicas de imputación
# identificación: isnull()
# para eliminación: dropna()
# para imputación, es como rellenar valores faltantes: fillna()


# Funciones lamda y apple

# Visualización avanzada con pandas y su integración con  otras librerias
# gráficas de puntos, histograma, grafico de barras como matlob






# FUNCIONES AVANZADAS DE PANDAS
import pandas as pd


ruta = "/home/alecc/Documentos/pandas_practice_orders.csv"
df = pd.read_csv(ruta)

# print("\nPrimeras 5 filas:")
# print(df.head())

# print("\nUltimas 5 filas:")
# print(df.tail())

# print("\nResumen estadistico:")
# print(df.describe())

# print("\nInformacion del DataFrame:")
# print(df.info())


"""
print("\nParte 1 - loc")

# Pedidos donde el neto sea mayor a 100
print(df.loc[df["net"] > 100])

# Mostrar columnas especificas
print(df.loc[0:5, ["order_id", "user_name", "net"]])

# Pedidos que fueron devueltos
print(df.loc[df["returned"] == True])


print("\nParte 2 - iloc")

# Primeras 5 filas
print(df.iloc[0:5])

# Filas 10 a 15 columnas 0 a 4
print(df.iloc[10:16, 0:5])

# Filas 0 a 5 columnas 0 a 4
print(df.iloc[0:5, 0:4])

# Solo primeras 3 columnas
print(df.iloc[:, 0:3])


print("\nParte 3 - query")

# Pedidos con net mayor a 100
print(df.query("net > 100"))

# Pedidos del segmento Consumer
print(df.query("segment == 'Consumer'"))

# Dos condiciones
print(df.query("net > 50 and payment_method == 'card'"))

# Dos condiciones 
print(df.query("discount > .1 and channel == 'web'"))

"""




"""
print("\nParte 5 - combinaciones complejas")

# loc con varias condiciones y columnas especificas
print(df.loc[
    (df["net"] > 50) & (df["payment_method"] == "card"),
    ["order_id", "user_name", "net", "payment_method"]
])

# loc con condicion y ordenamiento
print(df.loc[df["segment"] == "Consumer"]
      .sort_values("net", ascending=False))

# loc combinando tres condiciones
print(df.loc[
    (df["segment"] == "Consumer") &
    (df["net"] > 30) &
    (df["returned"] == False)
])


# iloc despues de ordenar
print(df.sort_values("net", ascending=False).iloc[0:5])

# iloc tomando filas especificas y columnas especificas
print(df.iloc[[0,5,10,15], [0,3,16]])

# iloc usando posicion despues de filtrar con loc
print(df.loc[df["net"] > 50].iloc[0:3])


# query con varias condiciones
print(df.query("segment == 'Consumer' and net > 50 and returned == False"))

# query combinada con ordenamiento
print(df.query("payment_method == 'card'")
      .sort_values("net", ascending=False))

# query combinada con seleccion de columnas
print(df.query("net > 40")[["order_id","user_name","net"]])

# query + loc combinados
print(df.query("segment == 'Corporate'")
      .loc[:, ["order_id","user_name","segment","net"]])


"""


"""
print("\nParte 6 - uso de variables")

# Variables para filtros
limite_net = 50
metodo_pago = "card"
segmento_cliente = "Consumer"
fila_inicio = 0
fila_fin = 5


# loc usando variables
print(df.loc[df["net"] > limite_net])

print(df.loc[df["payment_method"] == metodo_pago,
             ["order_id","user_name","payment_method","net"]])

print(df.loc[df["segment"] == segmento_cliente])


# iloc usando variables
print(df.iloc[fila_inicio:fila_fin])

columnas = [0,3,16]
print(df.iloc[fila_inicio:fila_fin, columnas])


# query usando variables (requiere @variable)
print(df.query("net > @limite_net"))

print(df.query("payment_method == @metodo_pago"))

print(df.query("segment == @segmento_cliente and net > @limite_net"))


# combinacion variables + ordenamiento
print(df.query("net > @limite_net")
      .sort_values("net", ascending=False))

"""




























print("\nSeccion - Agregacion y Groupby")

# Suma total de ventas netas
print("Suma total net:")
print(df["net"].sum())


# Promedio de ventas netas
print("\nPromedio net:")
print(df["net"].mean())


# Cantidad de pedidos
print("\nCantidad de pedidos:")
print(df["order_id"].count())


# Groupby por usuario (suma de compras)
print("\nTotal comprado por usuario:")
print(df.groupby("user_name")["net"].sum())


# Groupby por segmento (promedio de ventas)
print("\nPromedio net por segmento:")
print(df.groupby("segment")["net"].mean())


# Groupby por metodo de pago (cantidad de pedidos)
print("\nCantidad de pedidos por metodo de pago:")
print(df.groupby("payment_method")["order_id"].count())


# Groupby por ciudad (suma total)
print("\nTotal net por ciudad:")
print(df.groupby("city")["net"].sum())


# Groupby por categoria (promedio precio unitario)
print("\nPromedio unit_price por categoria:")
print(df.groupby("category")["unit_price"].mean())


# Groupby con dos columnas
print("\nTotal net por segmento y metodo de pago:")
print(df.groupby(["segment","payment_method"])["net"].sum())