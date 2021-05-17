import numpy as np

m = int(input('Valor de m: ')) 
n = int(input('Valor de n: ')) 
matriz = np.zeros((m, n))
vector = np.zeros((n))
x = np.zeros((m))
print('Introduce los valores')

for i in range (0, m):
    for j in range (0, n):
        matriz[(i),(j)] = (input("Elemento a [" + str(i+1) + "," + str(j+1) + "]: "))
        print (matriz)
    vector[(i)]=(input("b["+str(i+1)+"]: "))


#Aqui se obtiene los ceros debajo de la diagonal
for i in range (0, m):
    for j in range (i+1, m):
        factor = matriz[j,i]/matriz[i,i]
        vector[j] = vector[j] - (factor * vector[i])
        for x in range (0, n):
            matriz[j,x] = matriz[j,x] - (factor*matriz[i,x])

#sustitucion hacia atras

x[m-1] = vector[m-1]/matriz[m-1, m-1]
print(x[m-1])

for i in range(m-2, -1, -1):
    suma = 0
    for j in range(0, n):
        suma = suma + matriz[i,j]*x[j]
    x[i] = (vector[i]-suma)/matriz[i,i]

print('Resultado de la matriz')
print(matriz)
print("Resultado del vector")
print(vector)
print("Resultado: ")
print(x)