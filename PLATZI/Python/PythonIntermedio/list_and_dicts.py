def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"fistname": "Facundo", "lastname":"García"}

    super_lista = [
        {"fistname": "Facundo", "lastname":"García"},
        {"fistname": "Miguel", "lastname":"Torres"},
        {"fistname": "Edwin", "lastname":"Santiago"},
        {"fistname": "Jaret", "lastname":"Díaz"},
        {"fistname": "Hola", "lastname":"Torres"},
    ]

    super_dict = {
        "natual_nums" : [1,2,3,4,5],
        "integers_nums" : [-1,-2,0,1,2],
        "floating_nums" : [1.1,2.3,3.4,4.4,5.9],
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for values in super_lista:
        for key, value in values.items():
            print(key, "=", value)


if __name__ == '__main__':
    run()