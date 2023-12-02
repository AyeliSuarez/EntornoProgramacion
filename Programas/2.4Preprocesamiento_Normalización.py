# Ayeli Yaramit Suarez Soria, 951

import pandas as pd

datos = {'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril'], 'Ventas': [30500, 35600, 28300, 33900], 'Gastos': [22000, 23400, 18100, 20700]}
df = pd.DataFrame(datos)

normalizar = ['Ventas', 'Gastos']

# 1. Realizar una función que normalice los datos usando min-max que reciba como parámetro un DataFrame y otro
# parámetro que sea una lista de columnas a normalizar, retornar el DataFrame con los datos normalizados.

def min_max(df, columns):
    for column in columns:
        min_val = df[column].min()
        max_val = df[column].max()
        df[column] = (df[column] - min_val) / (max_val - min_val)
    return df

df_min_max = min_max(df.copy(), normalizar)
print("Min-Max Normalizado:\n", df_min_max)


# 2. Realizar una función que normalice los datos usando Z-Score que reciba como parámetro un DataFrame y otro
# parámetro que sea una lista de columnas a normalizar. Retornar el DataFrame con los datos normalizados
def z_score(df, columns):
    for column in columns:
        mean_val = df[column].mean()
        std_dev = df[column].std()
        df[column] = (df[column] - mean_val) / std_dev
    return df

df_z_score = z_score(df.copy(), normalizar)
print("\nZ-Score Normalizado:\n", df_z_score)


# 3. Realizar una función que normalice los datos usando escalado simple que reciba como parámetro un DataFrame y
# otro parámetro que sea una lista de columnas a normalizar. Retornar el DataFrame con los datos normalizados.
def simple_scale(df, columns):
    for column in columns:
        df[column] = df[column] / 1000
    return df

df_simple_scale = simple_scale(df.copy(), normalizar)

