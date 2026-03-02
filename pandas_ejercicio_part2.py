import pandas as pd
import os

ruta = "/home/alecc/Documentos/mineria_datos"

# =========================
# 1. Cargar los archivos
# =========================
orders_a = pd.read_csv(os.path.join(ruta, "part2_orders_a.csv"), parse_dates=["order_date"])
orders_b = pd.read_csv(os.path.join(ruta, "part2_orders_b.csv"), parse_dates=["order_date"])
customers = pd.read_csv(os.path.join(ruta, "part2_customers.csv"))
products = pd.read_csv(os.path.join(ruta, "part2_products.csv"))

# print("\n===== ORDERS_A =====")
# print(orders_a.head())

# print("\n===== ORDERS_B =====")
# print(orders_b.head())


# =========================
# 2. Unir orders_a y orders_b
# =========================
orders = pd.concat([orders_a, orders_b], ignore_index=True)

print("\n===== ORDERS UNIDOS (ÍNDICE REINICIADO) =====")
print(orders.head())
print("Total registros:", len(orders))


# =========================
# 3. Ordenar por order_date asc y qty desc
# =========================
orders_sorted = orders.sort_values(
    by=["order_date", "qty"],
    ascending=[True, False]
)

print("\n===== ORDENADO POR order_date ASC Y qty DESC =====")
print(orders_sorted.head())


# =========================
# 4. Establecer order_date como índice y ordenar cronológicamente
# =========================
orders_indexed = orders_sorted.set_index("order_date").sort_index()

print("\n===== order_date COMO ÍNDICE (ORDEN CRONOLÓGICO) =====")
print(orders_indexed.head())


# =========================
# 5. Merge con customers (left join, many_to_one)
# =========================
orders_customers = orders_indexed.merge(
    customers[["customer_id", "customer_name", "city", "segment"]],
    on="customer_id",
    how="left",
    validate="many_to_one"
)

print("\n===== MERGE CON CUSTOMERS =====")
print(orders_customers.head())


# =========================
# 6. Merge con products y calcular line_total
# =========================
orders_full = orders_customers.merge(
    products[["product_id", "product", "category", "unit_price"]],
    on="product_id",
    how="left",
    validate="many_to_one"
)

orders_full["line_total"] = orders_full["qty"] * orders_full["unit_price"]

print("\n===== MERGE CON PRODUCTS + line_total =====")
print(orders_full.head())


# =========================
# 7. Ordenar por line_total desc y mostrar top 5
# =========================
top5 = orders_full.sort_values(by="line_total", ascending=False).head(5)

print("\n===== TOP 5 POR line_total DESC =====")
print(top5)