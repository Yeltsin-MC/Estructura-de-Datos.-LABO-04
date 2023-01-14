import random
import numpy as np
A=[]
def pedir_filas():
    filas = int(input("Digite el número defilas:"))
    return filas


def pedir_columnas():
    columnas = int(input("Digite el número de columnas: "))
    return columnas


def llenar(matriz):
    filas = pedir_filas()
    columnas = pedir_columnas()
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            matriz[i].append(random.randint(1, 10))
    print(matriz)
def determinante_matriz(A):
    print("Matriz A con numpy")
    matriz_array = np.array(A)
    print(matriz_array)
    
    determinante = np.linalg.det(matriz_array)  #calcular la determinante
    print(round(determinante,0))
llenar(A)
determinante_matriz(A)