import math
entrada = input('')
numeroString = entrada.split(' ')
numeros = [float(x) for x in numeroString]
a, b, c = numeros

if (a < b):
	temp = a
	a = b
	b = temp

if (a < c):
	temp = a
	a = c
	c = temp

if (b < c):
	temp = b
	b = c
	c = temp

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
