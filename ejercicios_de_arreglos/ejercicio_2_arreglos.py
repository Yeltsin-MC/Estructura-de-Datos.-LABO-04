"""Dada las siguientes notas almacenadas en un arreglo:
[20, 15, 12, 11, 8, 4, 1]
Elimine la nota más baja programáticamente sin usar la
función (min) y escriba en pantalla.
Luego programáticamente calcule el promedio de notas
descontando la nota eliminada."""

notas=[20,15,11,8,4,1]
mayor=20
menor=mayor
for i in notas:
    if i < menor:
        menor =i
print(menor)

suma=0
lista_nueva=[]
for i in notas:
    if i== menor:
        continue
    else:
        suma+=i
        lista_nueva.append(i)       
print(suma/len(lista_nueva))
