import math

entrada = input("")
numeroscomString = entrada.split(" ")
numeros = [float(x) for x in numeroscomString]

a, b, c = numeros

delta = ((b * b) -4 * a * c)

if (delta >= 0) and (a != 0):

	r1 = (-b + (math.sqrt(delta))) / (2*a)
	r2 = (-b - (math.sqrt(delta))) / (2*a)
	print("R1 = %.5f" % r1)
	print("R2 = %.5f" % r2)

else:
	print("Impossivel calcular")
