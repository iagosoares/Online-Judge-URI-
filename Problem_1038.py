entrada = input("")
numerosString = entrada.split(" ")
numeros = [float(x) for x in numerosString]

a, b = numeros

if a == 1:
	total = b * 4.00
	print("Total: R$ %.2f" %total)

if a == 2:
	total = b * 4.50
	print("Total: R$ %.2f" %total)

if a == 3:
	total = b * 5.00
	print("Total: R$ %.2f" %total)

if a == 4:
	total = b * 2.00
	print("Total: R$ %.2f" %total)

if a == 5:
	total = b * 1.50
	print("Total: R$ %.2f" %total)
