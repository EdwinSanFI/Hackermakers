# I didnt check this code

def palindromeIndex(s):
    arreglo = {}
    arreglo2 = []
    j = -1
    # for i in s:
    #     j+=1
    #     if i not in arreglo:
    #         arreglo[j] = i
    #     else:
    #         arreglo2.append(i)
    # print(arreglo)
    # print(arreglo2)

    # for key,value in arreglo.items():
    #     if value not in arreglo2:
    #         return key
    for i in range(len(s)):
        if s[i] not in arreglo:
            arreglo[i] = s[i]
        else:
            arreglo2.append(i)

        print(arreglo2)
        print(arreglo)
print(palindromeIndex('aab'))