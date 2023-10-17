import pandas as pd

data = pd.read_csv("olimpiadas.csv",
                   index_col=0)

#print(data.sample(5))
datos_agrupados = data.groupby(["gender", "country"])
#print(datos_agrupados.get_group("female"))

columnas = ["gold", "silver", "bronze"]
#print(datos_agrupados[columnas].sum())

#print(res)

#print(data.country.value_counts())

#print(data.sort_values("year", ascending=False))

#print(data.mean(numeric_only=True))

#print(data.describe().transpose())

grupos = data.groupby(["gender", "country"])

#print(grupos.gold.mean().unstack())

#print(grupos.gold.mean())

pivot = data.pivot_table("gold", index="gender", columns="country", margins=True)
print(pivot)