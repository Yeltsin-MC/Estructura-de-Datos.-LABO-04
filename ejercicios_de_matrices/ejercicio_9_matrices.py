import numpy as np
import random


A=[[1,5],[5,1]]

def transpuesta(A):
    m = np.array(A)
    B = np.transpose(m)
    print(m)
    print(B)
    if np.array_equal(m,B) == True:
        print("Son transpuestas ")
    else:
        print("No son transpuestas ")
        
transpuesta(A)