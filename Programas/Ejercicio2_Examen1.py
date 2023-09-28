def div_5(lista):
    resultados = []
    for numero in lista:
        if numero % 5 == 0:
            resultados.append(True)
        else:
            resultados.append(False)

    return resultados


numeros = [10, 3, 5, 9, 15, 1]
resultados = div_5(numeros)
print(f"De la siguiente lista de numeros {numeros}, son divisibles en 5:")
print(resultados)
