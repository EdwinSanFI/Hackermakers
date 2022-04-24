def superDigit(n, k):
    suma = 0
    if k > 1:
        for i in range(k):
            suma += int(n[i])
        
        return superDigit(str(suma),len(str(suma))) + k
    
    return 0

if __name__ == '__main__':
    print(superDigit('4757362', 10000))