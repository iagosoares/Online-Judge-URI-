entrada = input('')
numeroString = entrada.split(' ')
numeros = [int(x) for x in numeroString]
x, y = numeros

if(x == y):
	print("O JOGO DUROU 24 HORA(S)")

if(x > y):
	aux = (y + 24) -x
	print("O JOGO DUROU {} HORA(S)".format(aux))

if(x < y):
	aux1 = y - x
	print("O JOGO DUROU {} HORA(S)".format(aux1))
