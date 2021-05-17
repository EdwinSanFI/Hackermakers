objeto = int(input('Escoja que programa ejecutuar [2, 3, 4] :'))

while abs(objeto == 2):
    objetivo = int(input('Escoge un numero : '))
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo: 
        print(abs(respuesta**2 - objetivo), respuesta)
    respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontró la raíz cuadrada del {objetivo}')
    else:
        print(f'La raíz cuadrada del objetivo {objetivo} es {respuesta}')

if objeto == 3:
    objetivo2 = int(input('Escoge un numero: '))
    epsilon = 0.01
    bajo = 0.0
    alto = max (1.0, objetivo2)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo2) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
    if respuesta**2 < objetivo2:
        bajo = respuesta
    else:
        alto = respuesta

    respuesta = (alto + bajo) /2

    print(f'La raiz cuadrada del {objetivo2} es {respuesta}')


if objeto == 4:
    objetivo3 = int(input('Escoge un entero: '))
    respuesta = 0

    while respuesta**2 < objetivo3:
        print(respuesta)
        respuesta += 1

    if respuesta**2 == objetivo3:
        print(f'La raiz cuadrada de {objetivo3} es {respuesta}')
    else: 
        print(f'{objetivo}3 no tiene una raiz cuadrada exacta')

else:
    print(f'No se puede realizar eso')
