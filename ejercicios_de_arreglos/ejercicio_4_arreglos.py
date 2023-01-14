"""Diseñe un programa que lea un vector y calcule si hay
un número que sea igual a la suma de los demás elementos
del vector."""

lista=[5,56,32,12,198,15,21,23,34]

for i in range(0,len(lista)):
    if lista[i] ==sum(lista[:i] +lista[i+1:]):
        print("Si hay un número de la lista que su valor es igual a la suma de los demás números, el número es: ", lista[i])
    else:
        print("no hay del numero:",lista[i] )
        