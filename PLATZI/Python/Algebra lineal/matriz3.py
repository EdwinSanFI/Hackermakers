import numpy as np

def run():

    A = np.zeros((columnas,filas))
    y = np.zeros((filas))

    for i in range (0, columnas):
        for j in range(0, filas):
            A[(i,j)] = int(input("Ingrese el valor de [" + str(i+1) + "][" + str(j+1) + "]"))
        y[(i)] = int(input("Ingrese el valor de B en posición [" + str(i+1) +"]"))

    # A = np.array([[2,-3,0],[4,-5,1],[2,0,4]]) 
    # y = np.array([[8] , [15], [1] ])

    for i in range (len(A)):
        print(A[i])
        print(y[i])

    if (np.linalg.det(A)) != 0.0 : 
        print("\nola, ME CHOCAS")
        print("\n Generamos la matriz Inversa \n") 
        B = np.linalg.inv(A)
        print(B)
        # print("\n Realizamos la multiplicación de la parte B por la matriz invertida de A \n") 
        # print(y*B)
        print("\n Siendo esto las variables de las incógnitas\n") 
        print(np.dot(B , y))
    else:
        print("\n La matriz de coeficientes es singular. \n") 
        print("\n No se puede encontrar una solución.\n")



if __name__ == "__main__":
    columnas = int(input('Ingrese el valor de columnas: '))
    filas = int(input('Ingrese el valor de filas: '))
    run()