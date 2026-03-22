import pandas as pd

data = {
    "Fruta": ["Manzana","Manzana","Manzana","Naranja","Naranja","Naranja"],
    "Color": ["Rojo","Rojo","Rojo","Naranja","Naranja","Naranja"]
}

df = pd.DataFrame(data)
print(df)
#=======================================
total_frutas = len(df)
prop_manzana = len(df[df['Fruta']== "Manzana"]) / total_frutas
prop_naranja = len(df[df['Fruta']== "Naranja"]) / total_frutas

print(f"P(Manzana) = {prop_manzana:.2f}")
print(f"P(Naranja) = {prop_naranja:.2f}")
 

#=======================================
manzanas = df[df['Fruta']== "Manzana"]
naranjas = df[df['Fruta']== "Naranja"]

#=======================================
p_rojo_manzana = len(manzanas[manzanas["Color"]=="Rojo"]) / len(manzanas)
#=======================================
p_naranja_naranja = len(naranjas[naranjas["Color"]=="Naranja"]) / len(naranjas)

print(f"P(Color = Rojo | Manzana) = {p_rojo_manzana:.2f}")
print(f"P(Color = Naranja | Naranja) = {p_naranja_naranja:.2f}")

#=======================================
nuevo_color = "Rojo"
p_manzan_rojo = (p_rojo_manzana * prop_manzana) / (p_rojo_manzana * prop_manzana + 0 * prop_naranja)
p_naranja_rojo = (0 * prop_manzana) / (p_rojo_manzana * prop_manzana + 0 * prop_manzana)

#=======================================
nuevo_color1 = "Naranja"
p_naranja_naranja = (p_naranja_naranja * prop_naranja) / (p_naranja_naranja * prop_naranja + 0 * prop_manzana)
p_manzana_naranja = (0 * prop_naranja) / (p_naranja_naranja * prop_naranja + 0 * prop_naranja)

#=======================================
if p_naranja_naranja > p_manzana_naranja:
    print(f"La fruta con color {nuevo_color1} es Naranja")
else:
    print(f"La fruta con color {nuevo_color1} es Manzana")
