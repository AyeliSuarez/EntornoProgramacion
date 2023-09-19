# Ayeli Yaramit Suarez Soria, 951, 27/08/23

import pandas as pd
import numpy as np

# 1 Crear DataFrame con los siguientes datos


datos = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril'],
    'Ventas': [30500, 35600, 28300, 33900],
    'Gastos': [22000, 23400, 18100, 20700]
}

dataframe = pd.DataFrame(datos)

# 2 Función que reciba el DataFrame, haga lista de meses, y devuelva el balance total


def calc_balance(dataframe, df_meses):
    dataframe_2 = dataframe[dataframe['Mes'].isin(df_meses)]
    balance = (dataframe_2['Ventas'] - dataframe_2['Gastos']).sum()
    return balance


meses_calculo = ['Enero', 'Febrero', 'Marzo', 'Abril']
balance_total = calc_balance(dataframe, meses_calculo)

print(f"Balance Total \nMeses: {', '.join(meses_calculo)} \nSuma Balance: {balance_total}")


# 3 Función que construya un Df a partir del archivo, devuelve otro Df con el mín, máx y la media de cada columna.


df_ibex35 = pd.read_csv("https://aprendeconalf.es/docencia/python/ejercicios/soluciones/pandas/cotizacion.csv",
                        sep=";", decimal=",")


def summarize_ibex35(df_ibex35):
    num = df_ibex35.select_dtypes(include=[float, int])
    summarize = {
        'Min': num.min(),
        'Max': num.max(),
        'Mean': num.mean()
    }

    df_summarize = pd.DataFrame(summarize)
    return df_summarize


df_resultado = summarize_ibex35(df_ibex35)
print(f"\n{df_resultado}")


# 4 Generar df, mostrar dimensiones, numero de datos con el nombre de su columna, 10 primeras y ultimas filas,
# % de personas que sobrevivieron y murieron, % de personas que sobrevivieron en cada clase.


df_titanic = pd.read_csv("https://aprendeconalf.es/docencia/python/ejercicios/soluciones/pandas/titanic.csv")

num_filas, num_columnas = df_titanic.shape
print(f"\nDimension DataFrame: {num_filas} filas, {num_columnas} columnas")
print("Primeras 10 filas:")
print(df_titanic.head(10))
print("\nÚltimas 10 filas:")
print(df_titanic.tail(10))

sobrevivieron = np.sum(df_titanic['Survived'] == 1)
murieron = np.sum(df_titanic['Survived'] == 0)
total_pasajeros = df_titanic.shape[0]

porcentaje_sobrevivieron = (sobrevivieron / total_pasajeros) * 100
porcentaje_murieron = (murieron / total_pasajeros) * 100

print(f"\nPorcentaje de personas que sobrevivieron: {porcentaje_sobrevivieron:.2f}%")
print(f"Porcentaje de personas que murieron: {porcentaje_murieron:.2f}%")

# Porcentaje de personas que sobrevivieron por cada clase
porcentaje_sobrevivieron_clase = df_titanic.groupby('Pclass')['Survived'].mean() * 100
print("\nPorcentaje de personas que sobrevivieron en cada clase:")
print(porcentaje_sobrevivieron_clase)
