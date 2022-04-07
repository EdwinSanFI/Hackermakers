def caesarCipher(s, k):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    n = len(alfabeto)
    s2=''
    for i in s:
        pos=alfabeto.find(i)
        return(pos)
        if pos>= 0:
            pos2 = (pos+k)%n
            i = alfabeto[pos2]
        s2+=i
    return s2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()