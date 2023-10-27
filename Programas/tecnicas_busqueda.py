import pandas as pd

alumnos = {
    "nombres": ["Juan", "Maria", "Pedro", "Miguel", "Test"],
    "edad": [20, 19, 22, 18, 100],
    "carrera": ["IN", "C", "NI", "IN", "LAE"],
    "promedio": [90, 85, 70, 100, 80]
}

df_alumnos = pd.DataFrame(alumnos)

# TECNICA 1, Filtrado de datos

c1 = df_alumnos.promedio > 80
data_c1 = df_alumnos[c1]
#print(data_c1)

columnas = ["nombres", "carrera"]
c2 = (df_alumnos.promedio > 80) & (df_alumnos.carrera.isin(["IN", "C"]))

data_c2 = df_alumnos[c2][columnas]
# print(data_c2)

# TECNICA 2, Busqueda por query

q1_c1 = df_alumnos.query("promedio > 80")
# print(q1_c1)

condicion = "promedio > 80 and carrera == 'IN' and carrera.isin(['IN', 'C'])"
q1_c2 = df_alumnos.query(condicion)[columnas]
print(q1_c2)
