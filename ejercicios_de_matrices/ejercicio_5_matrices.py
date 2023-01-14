
"""Suma, resta de matrices."""

A=[[25,35,62,41],[54,12,31,62],[65,85,45,61],[98,12,45,62]]
B=[[32,52,42,61],[62,12,23,21],[19,16,27,34],[24,26,31,39]]

def sumar_matrices(m1,m2):
    rpta=str(input("usted va sumar o restar?coloque: suma o resta :")) #aquí preguntamos si decea sumar o restar 
    if len(m1)==len(m2) and len(m1[0])==len(m2[0]):
        m3=[]
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m1[0])):

                if rpta=="suma":                          #aquí se realixa la condicional dependiendoa su respuesta(suma o resta)... 
                    m3[i].append(m1[i][j] + m2[i][j])
                else:
                    m3[i].append(m1[i][j] - m2[i][j])


        return m3
    else:
        return None

ma= sumar_matrices(A,B)
if ma==None:
    print("no se puede sumar")
else:
    for fila in ma:
        print("[", end=" ")
        for elemento in fila:
            print(elemento, end=" ")
        print("]")