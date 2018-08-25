#entrada
entrada = [int(i) for i in input().split()]
hi, mi, hf, mf = entrada

hora = hf - hi

if hora < 0:
	hora += 24

minuto = mf - mi

if minuto < 0:
	minuto += 60
	hora -= 1

if minuto == 0 and minuto == 0:
	print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
	print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(hora, minuto))
  
