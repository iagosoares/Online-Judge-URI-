import math

entrada = input()

numerosComString = entrada.split(" ")

numeros = [int(x) for x in numerosComString]

a, b, c = numeros

maiorAB = (a + b + abs(a-b))/2

maiorU = (maiorAB + c + abs(maiorAB - c))/2

print(int(maiorU), "eh o maior")
