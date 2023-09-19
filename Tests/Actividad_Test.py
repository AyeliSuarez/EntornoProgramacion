from Funciones import duplicados
from Funciones import suma
from Funciones import encripta
from Funciones import desencriptar
from Funciones import Pensionista, GrupoPensionistas
from Funciones import Estadistica

# import pytest


def test_duplicados():
    assert duplicados([1, 2, 3, 1]) == True
    assert duplicados([1, 2, 3, 4]) == False


def test_suma():
    assert suma([2, 7, 11, 15], 9) == [0, 1]


def test_encripta():
    clave = 'ixmrklstnuzbowfaqejdcpvhyg'
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    mensaje = "cafe"
    codificado_esperado = "milk"

    codificado_obtenido = encripta(mensaje, clave, alfabeto)
    assert codificado_obtenido == codificado_esperado


def test_desencriptar():
    clave = 'ixmrklstnuzbowfaqejdcpvhyg'
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    mensaje2 = "riok 1 mtfmfbidk"
    desencriptado_esperado = "dame 1 chocolate"

    desencriptado_obtenido = desencriptar(alfabeto, clave, mensaje2)
    assert desencriptado_obtenido == desencriptado_esperado


def test_pensionistas():
    persona1 = Pensionista('0001', 34, [640, 589, 573])
    persona2 = Pensionista('0002', 51, [865, 834, 798])
    persona3 = Pensionista('0003', 56, [487, 530, 660])

    grupo_pensionistas = GrupoPensionistas()
    grupo_pensionistas.agregar_pensionista(persona1)
    grupo_pensionistas.agregar_pensionista(persona2)
    grupo_pensionistas.agregar_pensionista(persona3)

    assert grupo_pensionistas.media_gastos('0001') == sum(persona1.gastos_mensuales) / len(persona1.gastos_mensuales)
    assert grupo_pensionistas.media_edad() == (persona1.edad + persona2.edad + persona3.edad) / len(grupo_pensionistas.pensionistas)
    assert grupo_pensionistas.edades_extrema() == (('0003', 56), ('0002', 51)) or (('0002', 51), ('0003', 56))
    assert grupo_pensionistas.suma_prom() == (sum(persona1.gastos_mensuales) / len(persona1.gastos_mensuales) +
                                              sum(persona2.gastos_mensuales) / len(persona2.gastos_mensuales) +
                                              sum(persona3.gastos_mensuales) / len(persona3.gastos_mensuales))
    max_media = max(sum(persona1.gastos_mensuales) / len(persona1.gastos_mensuales),
                    sum(persona2.gastos_mensuales) / len(persona2.gastos_mensuales),
                    sum(persona3.gastos_mensuales) / len(persona3.gastos_mensuales))
    assert grupo_pensionistas.media_max() == (persona2.identificador, persona2.edad, max_media)
    assert grupo_pensionistas.gasto_prom() == [559.0, 600.6666666666666, 832.3333333333334]


def test_estadistica():
    numeros = [1, 2, 3, 4, 2, 3, 5, 3, 3, 4, 4, 4]
    estadistica = Estadistica(numeros)
    assert estadistica.frecuenciaNumeros() == {1:1, 2:2, 3:4, 4:4, 5:1}
    assert estadistica.moda() == 3

# TODO: PENDIENTES
# @pytest.mark.parametrize("nums,res",
#                                [
#                                (1,2,3,1,True),
#                                (1, 2, 3, 4,False)
#                                ])
#
# def test_duplicados_parametrize(nums,res):
#    assert duplicados(nums) == res
