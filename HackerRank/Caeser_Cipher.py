def caesarCipher(s, k):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    alfabeto2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = len(alfabeto)
    s2=''
    for i in s:
        if i.isupper():
            pos=alfabeto2.find(i)
            if pos>= 0:
                pos2 = (pos+k)%n
                i = alfabeto2[pos2]
            s2+=i
        else:
            pos=alfabeto.find(i)
            if pos>= 0:
                pos2 = (pos+k)%n
                i = alfabeto[pos2]
            s2+=i
    return s2

if __name__ == '__main__':
    s = 'middle-Outz'
    k = 2
    result = caesarCipher(s, k)
    print(result)
    # Expected output: okffng-Qwvb