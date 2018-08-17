entrada  = input("")
numeroscomString = entrada.split(" ")
numeros = [int(x) for x in numeroscomString]

a, b, c, d = numeros

soma1 = c + d
soma2 = a + b

	
if (((b > c) and (d > a)) and (soma1 > soma2) and (c > 0 and d >0) and (a % 2 == 0)):
	print("Valores aceitos")
else:
	print("Valores nao aceitos")
