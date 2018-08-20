#Entrada
entrada = input('')
numeroString = entrada.split(' ')
numeros = [int(x) for x in numeroString]
a, b, c = numeros

#vetor ordenado
ordenado = []
ordenado = numeros
ordenado.sort()#usando metodo sort() da list

for x in ordenado:
	print('{}'.format(x))
#vetor original
print('')
print(a)
print(b)
print(c)
