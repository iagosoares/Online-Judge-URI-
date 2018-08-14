idade = int(input())

ano, mes, dia = 0, 0, 0

while idade >= 365:
   idade = idade - 365
   ano = ano + 1


while idade >= 30:
	idade = idade - 30
	mes = mes + 1

while idade > 0:
	idade = idade - 1
	dia = dia + 1

print(ano,"ano(s)")
print(mes,"mes(es)")
print(dia,"dia(s)")
