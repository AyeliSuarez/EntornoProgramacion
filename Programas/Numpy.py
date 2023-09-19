import numpy as np

list = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
n1 = np.array(list)
print(n1)
print(type(n1))

# Principales atributos
print(n1.ndim)
print(n1.shape)# Solo muestra un valor
print(n1.size)#Tamano de la lista
print(n1.dtype) #Tipo de dato

# Acceso a los elementos
print(n1[1, 2])

print(n1*2) # Multiplicar todos los elementos de la matriz
print(np.linalg.norm(n1)) #
print(n1.T) #Transpuerta
print(n1.mean())

# Ecuaciones
# x + 2y = 1
# 3x + 5y = 2

ecuaciones = [[1, 2], [3,   5]]

resultados = np.array([1, 2])
np_ecuaciones = np.array(ecuaciones)
print(np.linalg.solve(np_ecuaciones, resultados))
