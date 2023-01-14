""" Calcular la diagonal principal de una matriz """

import random
A = []


def pedir_f():
    filas = int(input("Digite el número de filas:"))
    return filas


def llenar_mostrar(matriz):
    filas = pedir_f()
    for i in range(filas):
        matriz.append([])
        for j in range(filas):
            matriz[i].append(random.randint(1, 10))
    print("matriz A")
    print(matriz)

    principal(filas)


def principal(filas):
    C = []
    for i in range(filas):
        C.append(A[i][i])
    print("Diagonal principal:")
    print(C)


llenar_mostrar(A)