import math

n = int(input()) 

hora = n // 3600

minutos = ((n/3600) - hora) * 60
minutos = (minutos // 1)

segundos = ((((n/3600) - hora) * 60) - minutos) * 60
segundos = round(segundos,4)
segundos = (segundos // 1)

print("%d:%d:%d" % (hora, minutos, segundos))
