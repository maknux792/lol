import numpy as np
matriz = np.array([[14,10,9,12],[6,5,7,15],[2,4,8,16],[1,3,11,13]])
print(matriz)
print("======================================")
print(matriz[2][1])
print("recorrer matriz")
for  n in range(4):
    for nn in range(4):
        print(matriz[n][nn])
        print("----------------")