sw =1



import numpy as np
matriz=np.array([[14.9,"bajo peso"],[24.9,"adecuado"],[29.9,"sobrepeso"],[34,9,"abesidad grado 1"],[39.9,"obesidad grado 2"],[40.0,"obesidad grado 3"]])
print(matriz)
while sw ==1:
    print("1.calcular_iva")
    print("2.descuento")
    print("3.calcular_imc")
    op=int(input("ingrese la opcion deseada:"))
    sw=0