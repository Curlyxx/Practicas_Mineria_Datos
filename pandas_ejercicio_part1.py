import pandas as pd

ruta = "/home/alecc/Documentos/part1_employees.csv"
df = pd.read_csv(ruta)

print("Ejercicio 1")
# Filas del depto Eng con perf_score >= 0.85
e1 = df[(df["dept"] == "Eng") & (df["perf_score"] >= 0.85)]
e1 = e1[["emp_id", "name", "city", "perf_score", "salary_mxn"]]
print(e1)


print("\nEjercicio 2")
# Filas 3 a 8 (incluye 3, excluye 8) columnas 0,1,5,6
e2 = df.iloc[3:8, [0,1,5,6]]
print(e2)


print("\nEjercicio 3")
# Empleados en CDMX o GDL con warnings = 0 y absences <=1
e3 = df[
    (df["city"].isin(["CDMX","GDL"])) &
    (df["warnings"] == 0) &
    (df["absences"] <= 1)
]

e3 = e3[["emp_id","name","city","warnings","absences"]]
print(e3)


print("\nEjercicio 4")
# Calculos con agg
e4 = df.agg({
    "salary_mxn":"mean",
    "perf_score":"mean",
    "warnings":"sum"
})

print(e4)


print("\nEjercicio 5")
# Estadisticas por departamento
e5 = df.groupby("dept").agg({
    "emp_id":"count",
    "salary_mxn":"mean",
    "perf_score":"mean"
})

print(e5)