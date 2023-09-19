import pandas as pd


datos = {"Articulo": ["Coca Cola", "Tostitos", "Cheetos", "Jugo"],
     "Precio": [17, 35, 20, 22],
     "Costo": [8, 17, 10, 11],
     "Categoria": ["Bebida", "Botanas", "Botana", "Bebida"]}


#objeto de la clase dataframe
data = pd.DataFrame(datos)
#print(data)

art = [
    ["Coca Cola", 17, 8, "Bebida"],
    ["Tostitos", 35, 17, "Botana"],
    ["Cheetos", 20, 12, "Botana"],
    ["Jugo", 22, 11, "Bebida"]
]
data2 = pd.DataFrame(art, columns=["Articulo", "Precio", "Costo", "Categoria"])
#print(data2)

# Seleccionar columna
#print(data.Articulo)

#class
#print(type(data["Articulo"]))

#seleccionar varias columnas
columnas = ["Articulo", "Precio"]
#print(data[columnas])

# Calcular utilidades de cada producto
utilidad = (data.Precio - data.Costo)
#agregar nueva columna
data["Utilidad"] = utilidad
#print(type(utilidad))

# Calcular que articulos tiene el precio mayor
max_precios = data.Precio.max()
#print(data.Precio == max_precios)
#mostrar renglones que cumplan con la condicion
#filtro = data.Precio == max_precios
#print(data[filtro])

#Solo imprimir columna
#print(data[filtro]["Articulo"])

#sin el sum
#print(data[filtro][columnas].sum())

#print(max_precios)

# Calcular que articulos tienen el precio mayor de la categoria bebida
data_filtrado = data[data.Categoria == "Bebida"]
maximo = data_filtrado.Precio.max()
# & and, | or
filtro = (data.Precio == maximo) & (data.Categoria == "Bebida")
#print(data[filtro][columnas])

# calcular max, min y prom de las columnas precio y costo, devolverlos en DF
columnas2 = ["Precio", "Costo"]
maximos = data[columnas2].max()
minimos = data[columnas2].min()
promedios = data[columnas2].mean()
res = pd.DataFrame([maximos, minimos, promedios], index =["Max","Min", "Mean"])
print(res)

#print(type(maximos))
#print(maximos)
#print(data)