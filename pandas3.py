import pandas as pd

ruta = "/home/alecc/Documentos/pandas_practice_orders.csv"
df = pd.read_csv(ruta)

g = df.groupby("city")
print(g)

g_keys = g.groups.keys()
print(g_keys)

g2 = df.groupby(["state", "channel"])

g2_keys = g2.groups.keys()
print(g2_keys)

#ventas netas

# Ventas netas por estado
# g3 = df.groupby("state")["net"].sum()

# print(g3)

# g3 = df.groupby("state")["net"].agg([
#     "sum",      # suma
#     "mean",     # promedio
#     "max",      # máximo
#     "min",      # mínimo
#     "count",    # cantidad de registros
#     "std",      # desviación estándar
#     lambda x: x.mode()[0]  # moda
# ])

# print(g3)



## Ordenacion de datos con sort value(), sort index()

# print(df.sort_values("net"))

# print(df.sort_index())

# print(df.sort_values("net", ascending=False))

# valores_cortos = df.sort_values(["net", "unit_price"], ascending=[True,False])
# print(valores_cortos.head())

# valores_cortos = df.sort_values("net", na_position=first)

valores_index =df.set_index("order_date")
# valores_index = df.sort_index()
# print(valores_index)

# con axis 1, ordena por columnas, con axis 0, por filas
df_colmuns = df.sort_index(axis=0)
print(df_colmuns.head())



#### FUNCION MERGE ####
print(df.info)

# crear nueva tabla de usuarios
users = df[["user_id", "user_name", "segment"]].drop_duplicates(subset=["user_id"])

print(users.head())


# Merge con la tabla original
df_merge = pd.merge(df, users, on="user_id")

print(df_merge.head())


a = df.iloc[:10]
b = df.iloc[10:]

reconstruido = pd.concat((a,b), ignore_index=True)
print(reconstruido)

