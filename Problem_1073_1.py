import math

entrada = int(input())

lista = []
if (entrada > 5) and (entrada < 2000):
    for cont in range(1, entrada + 1):
        lista.append(cont)

    for cont in lista:
        if (cont % 2 == 0):
            p = (cont * cont)
            print('{}^2 = {}'.format(cont, p))
