entrada = input("")
numeroString = entrada.split(" ")
numeros = [float(x) for x in numeroString]
x, y = numeros

if x > 0 and y > 0:
	print("Q1")

if x < 0 and y > 0:
	print("Q2")

if x < 0 and y < 0:
	print("Q3")

if x > 0 and y < 0:
	print("Q4")

if x == 0 and y != 0:
	print("Eixo Y")

if x != 0 and y == 0:
	print("Eixo X")	

if x == 0 and y == 0:
	print("Origem")		
