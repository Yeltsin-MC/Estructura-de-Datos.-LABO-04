"""multiplicación de matrices"""


A=[[25,35,62,41],[54,12,31,62],[65,85,45,61],[98,12,45,62]]
B=[[32,52,42,61],[62,12,23,21],[19,16,27,34],[24,26,31,39]]


def multiplicar_matrices(m1,m2):
    if len(m1[0])==len(m2):
        m3=[]
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m2[0])):
                m3[i].append(0)
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m1[0])):
                    print((i,j),(i,k),(j,k),(k,j))
                    m3[i][j]+= m1[i][k] * m2[k][j]
        return m3
    else:
        return None

ma= multiplicar_matrices(A,B)
if ma==None:
    print("no se puede multiplicar")
else:
    for fila in ma:
        print("[", end=" ")
        for elemento in fila:
            print(elemento, end=" ")
        print("]")