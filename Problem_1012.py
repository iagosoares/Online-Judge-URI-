entrada = input("")
numeroscomString = entrada.split(" ")
numeros = [float(x) for x in numeroscomString]

A, B, C = numeros
triangulo = (A * C) / 2
circulo = 3.14159 * (C * C)
trapezio = (A + B) / 2 * (C)
quadrado = B * B
retangulo = A * B

print("TRIANGULO: {:.3f}".format(triangulo))
print("CIRCULO: {:.3f}".format(circulo))
print("TRAPEZIO: {:.3f}".format(trapezio))
print("QUADRADO: {:.3f}".format(quadrado))
print("RETANGULO: {:.3f}".format(retangulo))
