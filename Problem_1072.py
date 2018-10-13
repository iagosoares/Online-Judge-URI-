entrada = int(input())

lista_entrada = []
for cont in range(0,entrada):
    valor = int(input())
    lista_entrada.append(valor)

i = 0
j = 0

for cont in lista_entrada:
    if (cont >= 10) and (cont <= 20):
        i += 1
    else:
        j += 1
        
print('{} in'.format(i))
print('{} out'.format(j))

# print('{} in\n{} out'.format(i,j))
