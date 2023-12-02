#Ayeli Yaramit Suarez Soria, 951
import pandas as pd

data = {
    'A': [1, 2, None, 4, 5],
    'B': [None, 7, 8, None, None],
    'C': [9, 10, 11, 12, 13],
}

df = pd.DataFrame(data)
#print(df)

# 1. función que reciba como parámetro un DataFrame y  retorne porcentaje de valores nulos
def porcentaje_nulos(df):
    return (df.isnull().sum() / len(df)) * 100

# 2. función que reciba como parámetro un DataFrame y retorne el número de renglones duplicados
def renglones_duplicados(df):
    return df.duplicated().sum()

# 3. función que reciba como parámetro un DataFrame y un máximo porcentaje. eliminar columnas que superen o igualen
# el máximo porcentaje de valores nulos establecidos. Retornar la lista nombres de columnas eliminadas.
# Validar que el porcentaje máximo esté entre 0 y 1.
def eliminar_columnas_nulos(df, max_porcentaje):
    if not 0 <= max_porcentaje <= 1:
        raise ValueError("Porcentaje máximo debe estar entre 0 y 1")

    eliminar_col = df.columns[df.isnull().mean() >= max_porcentaje]
    df = df.drop(columns=eliminar_col)

    return list(eliminar_col)

# 4. función que reciba como parámetro un DataFrame, una lista con los nombres de las columnas a verificar y una cadena.
# La cadena solo puede ser mean, bfill o ffill, en caso contrario una excepción.
# sustituir los valores nulos por el método especificado y retornar el DataFrame modificado.
def sustituir_nulos(df, columnas, metodo):
    if metodo not in ['mean', 'bfill', 'ffill']:
        raise ValueError("El método debe ser 'mean', 'bfill' o 'ffill'")
    if metodo == 'mean':
        df[columnas] = df[columnas].fillna(df[columnas].mean())
    elif metodo == 'bfill':
        df[columnas] = df[columnas].bfill()
    elif metodo == 'ffill':
        df[columnas] = df[columnas].ffill()

    return df

# 5. función que reciba como parámetro un DataFrame y elimine los renglones repetidos en el DataFrame Original.
# retornar la cantidad de renglones eliminados.
def eliminar_renglones_repetidos(df):
    antes = renglones_duplicados(df)
    df = df.drop_duplicates()
    despues = renglones_duplicados(df)

    renglones_eliminados = antes - despues
    return renglones_eliminados

# Pruebas de las funciones
print("\nPorcentaje de valores nulos por columna:")
print(porcentaje_nulos(df))

print("\nNúmero de renglones duplicados:")
print(renglones_duplicados(df))

max_porcentaje = 0.3
print(f"\nEliminando columnas con más del {max_porcentaje*100}% de valores nulos:")
columnas_eliminadas = eliminar_columnas_nulos(df, max_porcentaje)
print("Columnas eliminadas:", columnas_eliminadas)

df = sustituir_nulos(df, ['A', 'B'], 'mean')
print("\nDataFrame con valores nulos sustituidos:")
print(df)

renglones_eliminados = eliminar_renglones_repetidos(df)
print("\nRenglones duplicados eliminados:")
print(renglones_eliminados)
