def snail(snail_map):
    if snail_map == [[]]:
        return []
    else:
        map = []
        longitud = len(snail_map)
        i=0
        k=0
        iteraciones = 0
        tamano = len(snail_map) * len(snail_map)
        while iteraciones != tamano:
            # Derecha
            print("Derecha")
            for j in range(k, longitud):
                map.append(snail_map[i][j])
                iteraciones += 1
                print(snail_map[i][j])
                l = j

            i = l
            k+=1

            #Abajo
            print("Abajo")
            for j in range(k, longitud):
                map.append(snail_map[j][i])
                iteraciones += 1
                print(snail_map[j][i])

            k-= 1
            #Izquierda
            print("Izquierda")
            for j in range(longitud-1, k, -1):
                map.append(snail_map[i][j-1])
                iteraciones += 1
                print(snail_map[i][j-1])
                l = j

            i = l
            k+=1
            #Arriba
            print("Arriba")
            print("i", i)
            for j in range(longitud-1, k, -1):
                map.append(snail_map[j-1][i-1])
                iteraciones += 1
                print(snail_map[j-1][i-1])
            longitud -=1

        return(map)

if __name__ == '__main__':
    # array = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    # array = [[1,2,3],[4,5,6],[7,8,9]]
    array = [[]]
    print(snail(array))


#  Otra forma de hacerlo
# import numpy as np

# def snail(array):
#     m = []
#     array = np.array(array)
#     while len(array) > 0:
#         m += array[0].tolist()
#         array = np.rot90(array[1:])
#     return m

# def snail(array):
#     ret = []
#     if array and array[0]:
#         size = len(array)
#         for n in xrange((size + 1) // 2):
#             for x in xrange(n, size - n):
#                 ret.append(array[n][x])
#             for y in xrange(1 + n, size - n):
#                 ret.append(array[y][-1 - n])
#             for x in xrange(2 + n, size - n + 1):
#                 ret.append(array[-1 - n][-x])
#             for y in xrange(2 + n, size - n):
#                 ret.append(array[-y][n])
#     return ret

# def snail(array):
#     out = []
#     while len(array):
#         out += array.pop(0)
#         array = list(zip(*array))[::-1] # Rotate
#     return out

# my implementation/explanation of the solution by foxxyz
# S