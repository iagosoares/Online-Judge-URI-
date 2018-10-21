entrada = int(input())

lista_entrada = []
if(entrada > 0) and (entrada < 10000):
	for cont in range(1,10001):
		lista_entrada.append(cont)

for cont in lista_entrada:
	if(cont % entrada == 2):
		print(cont)
