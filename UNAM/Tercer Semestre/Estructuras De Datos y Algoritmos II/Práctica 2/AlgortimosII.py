##################################
# @author: Edwin Santiago
# Se implementan 2 algoritmos (QuickSort y HeapSort)
# Con una lista de 10 números aleatorios del 0 al 10
# Y se mide el tiempo que tarda cada algoritmo
##################################

# Se importa de la libreria "time" la funcion "perf_counter"
# para calcular el tiempo que tardan en ordenar cada algoritmo
from random import randint
from time import perf_counter

# Algoritmo: Quick Sort
# Recibe como parametro la lsita de numeros, el indice del primer elemento de la lista y el tamaño de la lista
def quickSort(a, p, r):
    # Revisa que la lsita tenga más de 1 elemento
    if p < r:
        # Divide la lista y nos da la posicion del pivote
        q = patrocinar(a,p,r)
        # Subarreglo de la parte izquierda
        quickSort(a, p, q-1)
        # Subarreglo de la parte derecha
        quickSort(a,q+1, r)

# La funcion reacomoda los subarreglos donde ambas partes (izq y der) esten acomoaddos conforme al pivote
# Recibe como parametro la lista de numeros, el indice del primer elemento y el tamaño de la lista
def patrocinar(a, p, r):
    # Para evitar que el algoritmo caiga en el peor de los casos se escoge un pivote al azar
    rand = randint(p,r)
    # Y se intercambia de valor con el ultimo elemento
    # Con esto, se optimiza el algoritmo y puede ordenar listas hasta de 20k elementos
    a[rand], a[r] = a[r], a[rand]
    # Es el elemento pivote (ultimo elemento aunque puede variar)
    x=a[r]
    # Indice auxuliar
    i = p-1


    # Compara todos los elementos para saber cuales son menores y mayores que el pivote
    for j in range(p,r):
        # Intercambia el valor para que quede del lado izquierdo del arreglo los menores o iguales al pivote
        if a[j] <= x:
            i+= 1
            a[i], a[j] = a[j], a[i]

    # El pivote cambia de posicion para marcar la division de menores y mayores a el
    a[i+1], a[r] = a[r], a[i+1]
    # Retorna la posicion final del pivote.
    return i+1

# Algoritmo: Heap Sort
# Recibe como parametro el arreglo de numeros
def ordenacionHeapSort(a):
    construirHeapMaxIni(a)
    # Guarda el numero de elementos del arreglo
    tamañoHeap = len(a)
    for i in range(len(a)-1,0,-1):
        a[0], a[i] = a[i], a[0]
        tamañoHeap -=1
        maxHeapify(a,0,tamañoHeap)

# Construye el heap inicial de forma que sea un HeapMaixmo
def construirHeapMaxIni(A):
    tamañoHeap = len(A)
    for i in range(len(A) // 2, -1, -1):
        maxHeapify (A, i, tamañoHeap)

def maxHeapify(A, i, tamañoHeap):
    L = 2*i +1
    R = 2*i+2

    posMax = i
    # Si A[i] es mayor o igual a la info almacenada en la raiz de sub.zq.
    # y derecho entonces el arbol con raiz en el nodo I es un HeapMaximo y la funcion termina
    # De lo contrario, la raiz de alguno subarbol es mayor a A[i] y es intercambiada con esta
    if L < tamañoHeap and A[L] > A[i]:
        posMax = L
    if R < tamañoHeap and A[R] > A[posMax]:
        posMax = R

    if posMax != i:
        # Intercambia los valores
        A[i], A[posMax] = A[posMax], A[i]
        # Permite que el heap modificado mantenga la propiedad de orden de un HeapMaximo
        #A[i] acomoda para que el arbol siga cumpliendo con que la raiz de cada subarbol es mayor o igual que sus nodos restantes
        maxHeapify(A, posMax, tamañoHeap)

def run():

    print("Practica 2")
    print("Ejercicio 2\n")

    arregloQuickSort = [7,3,1,9,2,3,5,4,6,8]
    arregloHeapSort = [7,3,1,9,2,3,5,4,6,8]

    print("Arreglo desordenado: ", arregloHeapSort)

    # Se inicializa el cronómetro
    tiempoInicial1 = perf_counter()
    # Se ejecuta el algoritmo
    ordenacionHeapSort(arregloQuickSort)
    # Se detiene el cronómetro
    tiempoFinal1 = perf_counter()
    #Se calcula el tiempo tomado a completar el algoritmo
    tiempo1 = tiempoFinal1 - tiempoInicial1

    # Se inicializa el cronómetro
    tiempoInicial2 = perf_counter()
    # Se ejecuta el algoritmo
    quickSort(arregloHeapSort,0,len(arregloHeapSort)-1)
    # Se detiene el cronómetro
    tiempoFinal2 = perf_counter()
    #Se calcula el tiempo tomado a completar el algoritmo
    tiempo2 = tiempoFinal2 - tiempoInicial2

    print("Lista ordenada por QuickSort: ", arregloQuickSort)
    print("El algoritmo tardó: {:.8f}".format(tiempo1))
    print("Lista ordenada por HeapSort: ",arregloHeapSort)
    print("El algoritmo tardó: {:.8f}".format(tiempo2))

if __name__ == '__main__':
    run()