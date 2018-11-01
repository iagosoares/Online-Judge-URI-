n = int(input())
lista = []

for cont in range(n):
	entrada = input().split()
	lista.append(entrada)

rato = []
sapo = []
coelho = []

for cont in range(n):
	if lista[cont][1] == 'R':
		rato.append(int(lista[cont][0]))
		
	if lista[cont][1] == 'S':
		sapo.append(int(lista[cont][0]))
		
	if lista[cont][1] == 'C':
		coelho.append(int(lista[cont][0]))

soma_coelhos = sum(coelho)
soma_ratos = sum(rato)
soma_sapos = sum(sapo)

total = soma_coelhos + soma_ratos + soma_sapos

percentual_coelho = (soma_coelhos * 100)/total 
percentual_rato = (soma_ratos * 100)/total
percentual_sapo = (soma_sapos * 100)/total


print('Total: {} cobaias'.format(total))
print('Total de coelhos: {}'.format(sum(coelho)))
print('Total de ratos: {}'.format(sum(rato)))
print('Total de sapos: {}'.format(sum(sapo)))
print('Percentual de coelhos: {:.2f} %'.format(percentual_coelho))
print('Percentual de ratos: {:.2f} %'.format(percentual_rato))
print('Percentual de sapos: {:.2f} %'.format(percentual_sapo))
