import numpy as np
from scipy.linalg import inv

print("Este es un programa encargado de hallar inversas de una matriz")
filas=int(input("Ingrese el número de filas de la matriz:"))
Columnas= int(input("Ingrese el número de columnas de la matriz:"))

if filas != Columnas:
    print("La matriz debe ser cuadrada para porder hallar una inversa")
else:
    print("Ingrese los elementos de la matriz fila por fila(separados por espacios)")
    matriz=[]

    for i in range(filas):
        fila =list(map(float,input(f"Fila {i+1}:").split()))
        if len(fila)!= Columnas:
            print ("Numero incorrecto de elementos, intente de nuevo.")
            exit()
        matriz.append(fila)
    
    matriz_np =np.array(matriz)

    try:
        inversa = inv(matriz_np)
        print("Matriz original:")
        print(matriz_np)
        print("Matriz inversa:")
        print(inversa)
    except np.linalg.LinAlgError:
        print("La matriz no es invertible")

