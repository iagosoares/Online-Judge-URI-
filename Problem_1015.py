import math

p1 = input()
p2 = input()

stringP1 = p1.split(" ")
stringP2 = p2.split(" ")

entrada_1 = [float(x) for x in stringP1]
entrada_2 = [float(x) for x in stringP2]

x1, y1 = entrada_1
x2, y2 = entrada_2

distancia = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2) )

print("{:.4f}".format(distancia))
