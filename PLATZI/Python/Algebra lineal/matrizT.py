import numpy as np
A = np.array([[2,-3,0],[4,-5,1],[2,0,4]]) 
y = np.array([[8] , [15], [1] ])
if (np.linalg.det(A)) != 0.0 : 
    print("\nola, ME CHOCAS")
    print("\n Generamos la matriz Inversa \n") 
    B = np.linalg.inv(A)
    print(B)
    print("\n Mostramos la multiplicación de y*inv(A) \n") 
    print(y*B)
    print("\n lo cual resuelve la ecuación. \n") 
    print(np.dot(B , y))
else:
    print("\n La matriz de coeficientes es singular. \n") 
    print("\n No se puede encontrar una solución.\n")