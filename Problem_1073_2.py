import math

entrada = int(input())

if (entrada > 5) and (entrada < 2000):
    for cont in range(1, entrada + 1):
        if (cont % 2 == 0):
            p = pow(cont,2)
            print('{}^2 = {}'.format(cont,p))
