def run():

    # my_dict = {}
    # for i in range(1, 101):
    #     if i%3 != 0:
    #         my_dict[i] = i**3
    # print(my_dict)


    dic = {i: i**3 for i in range (1,101) if i %3 !=0}
    print(dic)
    #reto 
    #para redondear la raiz cuadrada se puede utilizar
    #round(i**0.5, 2)
    my_dic = {i: i**0.5 for i in range (1,1001)}
    print(my_dic)

if __name__ == '__main__':
    run()