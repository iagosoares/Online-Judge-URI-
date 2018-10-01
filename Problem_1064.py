e1 = float(input())
e2 = float(input())
e3 = float(input())
e4 = float(input())
e5 = float(input())
e6 = float(input())
entrada = [e1, e2, e3, e4, e5, e6]
i = 0
positivos = []
for n in entrada:
    if (n > 0):
        positivos.append(n)
        i = i + 1
            
soma = sum(positivos)
tamanho_lista = len(positivos)
media = soma / tamanho_lista

print('{} valores positivos'.format(i))
print('{:.2f}'.format(media))
