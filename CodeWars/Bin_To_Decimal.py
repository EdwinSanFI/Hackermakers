def bin_to_decimal(inp):
    sum = 0
    j = len(inp)-1
    for i in range(len(inp)):
        if int(inp[i]) == 1:
            sum += 2**j
        j-=1
    return sum

if __name__ == '__main__':
    print(bin_to_decimal('101'))

# Pruebas
# 1101001011111110001000 3456904
# 10000101111101100000110 4389638
# 10000010111101010101111 4291247
# 1111101111101100001000 4127496
# 1000011101011111011010 2217946
# 110101100011000100110 1754662

# Otras soluciones
#1
def bin_to_decimal(inp):
    return int(inp, 2)

#2
def bin_to_decimal(inp):
    num = 0
    inp = inp[::-1]
    for i in range(len(inp)):
        num += int(inp[i]) * 2 ** i
    return num

#3
bin_to_decimal = lambda inp: int(inp,2)