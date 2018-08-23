import math
entrada = input('')
numeroString = entrada.split(' ')
numeros = [float(x) for x in numeroString]
x, y, z = numeros

if (x,y,z > 0):

	lista = []
	lista = numeros
	lista.sort()

	a = lista[2]
	b = lista[1]
	c = lista[0]

if (a >= (b + c)):
	print('NAO FORMA TRIANGULO')
else:

	if (a * a == b*b + c*c):
		print('TRIANGULO RETANGULO')

	if (a * a > b*b + c*c):
		print('TRIANGULO OBTUSANGULO')

	if (a * a < b*b + c*c):
		print('TRIANGULO ACUTANGULO')

	if (a==b and a==c and b==c):
		print('TRIANGULO EQUILATERO')
	else:
		if (a==b or a==c or b==c):
			print('TRIANGULO ISOSCELES')
