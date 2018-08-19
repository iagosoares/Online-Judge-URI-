entrada = input("")
numerosString = entrada.split(" ")
numeros = [float(x) for x in numerosString]

n1, n2, n3, n4 = numeros

media = (n1*0.2 + n2*0.3 + n3*0.4 + n4*0.1)
media = float("%.2f" % media)

if(media >= 7.0):
	print("Media:",media)
	print("Aluno aprovado.")

if(media < 5.0):
	print("Media: %.1f"%media)
	print("Aluno reprovado.")
else:

	if (media >= 5.0) and (media < 7.0):
		print("Media:",media)
		print("Aluno em exame.")
		notaexame = float(input(""))
		print("Nota do exame:",notaexame)


		mediax = (notaexame + media) / 2.0

		if mediax >= 5.0:
			print("Aluno aprovado.")

		if mediax < 5.0:
			print("Aluno reprovado.")

		print("Media final:",mediax)
