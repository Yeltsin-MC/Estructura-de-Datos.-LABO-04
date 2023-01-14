"""Crea dos arrays o arreglos unidimensionales que tengan
el mismo tamaño (lo pedirá por teclado), en uno de ellos
almacenarás nombres de personas como cadenas, en el
otro array o arreglo ira almacenando la longitud de los
nombres..."""

n = int(input("Ingrese el tamaño de los arreglos:"))
lista1 = [] #f
lista2 = []
for i in range (0,n):
 lista1.append(input("Ingrese nombre de las personas:"))
print(lista1)
for j in range (0,n):
 lista2.append(len(lista1[j]))
print(lista2)