n = int(input())

lista_entrada = []
if(n > 0) and (n < 10000):
	for cont in range(0, n):
		x = int(input())
		lista_entrada.append(x)

for cont in lista_entrada:
	if(cont > 0) and (cont % 2 == 0):
		print('EVEN POSITIVE')
	elif(cont < 0) and (cont % 2 == 0):
		print('EVEN NEGATIVE')
	if(cont > 0) and (cont % 2 != 0):
		print('ODD POSITIVE')
	elif(cont < 0) and (cont % 2 != 0):
		print('ODD NEGATIVE')
	if(cont == 0):
		print('NULL')
