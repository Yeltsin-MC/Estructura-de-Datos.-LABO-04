"""Crea un array o arreglo unidimensional donde le indiques
el tamaño por teclado y crear una función que rellene
el array o arreglo con los múltiplos de un número pedido
por teclado.

Por ejemplo, si defino un array de tamaño 5 y elijo un
3 en la función, el array contendrá 3, 6, 9, 12, 15.
Muéstralos por pantalla usando otra función distinta."""

def rellenador_multiplos(a,b):
    for i in range(1,a+1):
        lista.append(i*b)
    return lista

def leer_lista(lista):
    print(lista)

lista=[]

n = int(input("Ingrese el tamaño de los arreglos:"))
n1=int(input("Ingrese el numero para conocer sus primeros n multiplos:"))

rellenador_multiplos(n,n1)
leer_lista(lista)