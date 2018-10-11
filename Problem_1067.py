x = int(input(''))

if(x >= 1) and (x <=1000):

	lista = []
	for c in range(x+1):
		lista.append(c)
p = []
for y in lista:
	if y % 2 != 0:
		p.append(y)
		print(y)
