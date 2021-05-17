def run():
    # lista = []
    # for i in range(101): #range(1, 101)
    #     i = i**2
    #     if i % 3 != 0:
    #         lista.append(i) #otra opcion
    #     #lista.append(i**2)
    # print(lista)    
    #ESTO ES ANTES DE VER LIST COMPREHENSIONS
    
    #for i in range (1, 101):
        #if i % 3 != 0:
            #lista.append(i**2)

    lista = [i**2 for i in range(1, 101) if i%3 != 0]
    print(lista)
    #reto
    otra = [i for i in range(1, 10000) if i%4==0 and i%6==0 and i%9==0]
    print(otra)

if __name__ == '__main__':
    run()