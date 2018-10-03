valores = []
for x in range(0,5):
	entrada = int(input())
	valores.append(entrada)

i = 0
j = 0
k = 0
h = 0

for y in valores:
	if ((y % 2) == 0):
		i = i + 1
	else:
		j = j + 1

	if (y > 0):
		k = k + 1

	if (y < 0):
		h = h + 1

print('{} valor(es) par(es)'.format(i))
print('{} valor(es) impar(es)'.format(j))
print('{} valor(es) positivo(s)'.format(k))
print('{} valor(es) negativo(s)'.format(h))
