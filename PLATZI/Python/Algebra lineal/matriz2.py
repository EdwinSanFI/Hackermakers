import numpy as np


def escoger():
    if (opcion == "1"):
        operaciones()
    elif (opcion == "2"):
        run()
    else:
        print("No se reconoce ese valor")


def operaciones():
    matrices = int(input('Ingrese la cantidad de matrices: '))
    columnas = int(input('Ingrese el valor de columnas: '))
    filas = int(input('Ingrese el valor de filas: '))
    A = np.zeros((columnas,filas))
    ma = np.array((matrices))
    suma = ma[(matrices-1)] + ma[(matrices)]
    resta = ma[(matrices-1)] - ma[(matrices)]
    multi = ma[(matrices-1)] * ma[(matrices)]

    for g in range (matrices):
        print('Ingrese los valores de la matriz [' + str(matrices-1) + ']')
        ma = np.array((A))
        for i in range (0, columnas):
            for j in range(0, filas):
                A[(i,j)] = int(input("Ingrese el valor de [" + str(i+1) + "][" + str(j+1) + "]"))
        print(A)
        # ma[(g)] = A

    # for i in range (len(matrices-1)):
        suma = ma[(matrices)] + ma[(matrices+1)]
        resta = ma[(matrices)] - ma[(matrices+1)]
        multi = ma[(matrices)] * ma[(matrices+1)]

    print(suma)
    print(resta)
    print(multi)


def run():

    columnas = int(input('Ingrese el valor de columnas: '))
    filas = int(input('Ingrese el valor de filas: '))

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
    print("Bienvenido a la calculadora de matrices :D")
    print("Favor de seleccionar la tarea a realizar")
    print("1) Operaciones entre 2 matrices (Suma, Resta y Multiplicación)")
    print("2) Encontrar las variables de la matriz")
    opcion = input("Ingrese el número: ")
    escoger()


