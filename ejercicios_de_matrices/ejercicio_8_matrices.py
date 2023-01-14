import numpy as np
import random
A=[]
def pedir_filas():
    filas = int(input("Digite el número de filas:"))
    return filas


def pedir_columnas():
    columnas = int(input("Digite el númerode columnas: "))
    return columnas


def llenar(matriz):
    filas = pedir_filas()
    columnas = pedir_columnas()
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            matriz[i].append(random.randint(1, 10))
    print(matriz)

def transpuesta(A):
    matriz1 = np.array(A)
    matriz2 = np.transpose(matriz1)
    print(matriz2)

llenar(A)
transpuesta(A)