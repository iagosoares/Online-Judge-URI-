valores = []
for x in range(0,5):
	entrada = int(input())
	valores.append(entrada)

i = 0
for y in valores:
	if ((y % 2) == 0):
		i = i + 1
print('{} valores pares'.format(i))
