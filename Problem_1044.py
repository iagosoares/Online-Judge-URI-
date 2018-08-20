entrada = input('')
numeroString = entrada.split(' ')
numeros = [float(x) for x in numeroString]
x, y = numeros

if (x % y == 0) or (y % x == 0):
	print('Sao Multiplos')
else:
	print('Nao sao Multiplos')
