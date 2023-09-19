# Ayeli Yaramit Suarez Soria, 952
# 15 de agosto de 2023


# Ejercicio 1
nums = [1, 2, 3, 1]


def duplicados(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


print(duplicados(nums))


# Ejericio 2
lista = [2, 7, 11, 15]
target = 9


def suma(lista, target):
    dicc = {}
    for i, num in enumerate(lista):
        n = target - num
        if n not in dicc:
            dicc[num] = i
        else:
            return [dicc[n], i]


print(suma(lista, target))

# Ejercicio 3

clave = 'ixmrklstnuzbowfaqejdcpvhyg'
mensaje = "cafe"
alfabeto = 'abcdefghijklmnopqrstuvwxyz'


def encripta(s, clave, alfabeto):
    x = str.maketrans(alfabeto, clave)
    codificado = s.translate(x)
    return codificado


codificado = encripta(mensaje, clave, alfabeto)
print(codificado)

# Ejercicio 4
mensaje2 = 'riok 1 mtfmfbidk'


def desencriptar(alfabeto, clave, s):
    y = str.maketrans(clave, alfabeto)
    descodificado = s.translate(y)
    return descodificado


descodificado = desencriptar(alfabeto, clave, mensaje2)
print(descodificado)

# Ejercio 5


class Pensionista:
    def __init__(self, identificador, edad, gastos_mensuales):
        self.identificador = identificador
        self.edad = edad
        self.gastos_mensuales = gastos_mensuales


class GrupoPensionistas:
    def __init__(self):
        self.pensionistas = []

    def agregar_pensionista(self, pensionista):
        self.pensionistas.append(pensionista)

    def media_gastos(self, identificador):
        for pensionista in self.pensionistas:
            if pensionista.identificador == identificador:
                return sum(pensionista.gastos_mensuales) / len(pensionista.gastos_mensuales)
        return None

    def media_edad(self):
        total_edades = sum(p.edad for p in self.pensionistas)
        return total_edades / len(self.pensionistas)

    def edades_extrema(self):
        pensionista_menor_edad = min(self.pensionistas, key=lambda p: p.edad)
        pensionista_mayor_edad = max(self.pensionistas, key=lambda p: p.edad)
        return (pensionista_menor_edad.identificador, pensionista_menor_edad.edad), (
            pensionista_mayor_edad.identificador, pensionista_mayor_edad.edad)

    def suma_prom(self):
        suma_promedios = sum(sum(p.gastos_mensuales) / len(p.gastos_mensuales) for p in self.pensionistas)
        return suma_promedios

    def media_max(self):
        max_media = -1
        max_pensionista = None
        for pensionista in self.pensionistas:
            media = sum(pensionista.gastos_mensuales) / len(pensionista.gastos_mensuales)
            if media > max_media:
                max_media = media
                max_pensionista = pensionista
        return max_pensionista.identificador, max_pensionista.edad, max_media

    def gasto_prom(self):
        return sorted([sum(p.gastos_mensuales) / len(p.gastos_mensuales) for p in self.pensionistas])


persona1 = Pensionista('0001', 34, [640, 589, 573])
persona2 = Pensionista('0002', 51, [865, 834, 798])
persona3 = Pensionista('0003', 56, [487, 530, 660])

# Crear objeto de GrupoPensionistas y agregar pensionistas
grupo_pensionistas = GrupoPensionistas()
grupo_pensionistas.agregar_pensionista(persona1)
grupo_pensionistas.agregar_pensionista(persona2)
grupo_pensionistas.agregar_pensionista(persona3)

# Ejemplos de uso de los métodos
print("\nMedia de gastos de '0001':", grupo_pensionistas.media_gastos('0001'))
print("Media de edades:", grupo_pensionistas.media_edad())
print("Edades extremas:", grupo_pensionistas.edades_extrema())
print("Suma promedio de gastos:", grupo_pensionistas.suma_prom())
print("Media máxima de gastos:", grupo_pensionistas.media_max())
print("Gasto promedio:", grupo_pensionistas.gasto_prom())


# Ejercicio 6

class Estadistica:
    def __init__(self, numeros):
        self.numeros = numeros

    def frecuenciaNumeros(self):
        frecuencia = {}
        for numero in self.numeros:
            frecuencia[numero] = frecuencia.get(numero, 0) + 1
        return frecuencia

    def moda(self):
        frecuencia = self.frecuenciaNumeros()
        moda = max(frecuencia, key=frecuencia.get)
        return moda

    def histograma(self):
        frecuencia = self.frecuenciaNumeros()
        for numero, freq in frecuencia.items():
            print(f"{numero}: {'*' * freq}")

# Ejemplo de uso
numeros = [1, 2, 3, 4, 2, 3, 5, 3, 3, 4, 4, 4]
estadistica = Estadistica(numeros)

print("\nFrecuencia de números:", estadistica.frecuenciaNumeros())
print("Moda:", estadistica.moda())
print("Histograma:")
estadistica.histograma()

