salario = float(input(''))
# numeroString = entrada.split(' ')
# numeros = [float(x) for x in numeroString]
# salario = numeros

if (salario >= 0.00) and (salario <= 400.00):
	reajuste = salario * 0.15
	novosalario = (salario * 0.15) + salario
	print('Novo salario: {:.2f}'.format(novosalario))
	print('Reajuste ganho: {:.2f}'.format(reajuste))
	print('Em percentual: 15 %')

if (salario >= 400.01) and (salario <= 800.00):
	reajuste = salario * 0.12
	novosalario = (salario * 0.12) + salario
	print('Novo salario: {:.2f}'.format(novosalario))
	print('Reajuste ganho: {:.2f}'.format(reajuste))
	print('Em percentual: 12 %')

if (salario >= 800.01) and (salario <= 1200.00):
	reajuste = salario * 0.10
	novosalario = (salario * 0.10) + salario
	print('Novo salario: {:.2f}'.format(novosalario))
	print('Reajuste ganho: {:.2f}'.format(reajuste))
	print('Em percentual: 10 %')
 
if (salario >= 1200.01) and (salario <= 2000.00):
	reajuste = salario * 0.07
	novosalario = (salario * 0.07) + salario
	print('Novo salario: {:.2f}'.format(novosalario))
	print('Reajuste ganho: {:.2f}'.format(reajuste))
	print('Em percentual: 7 %')

if (salario > 2000.00):
	reajuste = salario * 0.04
	novosalario = (salario * 0.04) + salario
	print('Novo salario: {:.2f}'.format(novosalario))
	print('Reajuste ganho: {:.2f}'.format(reajuste))
	print('Em percentual: 4 %')
