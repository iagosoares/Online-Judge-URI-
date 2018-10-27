lista = []
while len(lista) != 100:    
    aux = int(input())
    if (aux not in lista) and (aux >= 0):
        lista.append(aux)
        maior = max(lista)
        indice = lista.index(maior)

print(maior)
print('{}'.format(indice+1))
