import math
#Entrada
entrada = input('')
numeroString = entrada.split(' ')
numeros = [float(x) for x in numeroString]
a, b, c = numeros
##########################################
if (abs(b - c) < a) and (a < (b + c)):

	if (abs(a - c) < b) and (b < (a + c)):

		if (abs(a - b) < c) and (c < (a + b)):
				
			perimetro = (a + b + c)
			print('Perimetro = {:.1f}'.format(perimetro))

else:
	area = ((a + b) * c) / 2
	print('Area = {:.1f}'.format(area))
