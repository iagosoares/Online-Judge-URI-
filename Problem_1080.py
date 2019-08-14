#Solution 1 -----> Don't accept for URI
lista = []
while len(lista) != 100:    
    aux = int(input())
    if (aux not in lista) and (aux >= 0):
        lista.append(aux)
        maior = max(lista)
        indice = lista.index(maior)

print(maior)
print('{}'.format(indice+1))

#-------------------------------------------------------------------------

# Solution 2 ------->Accept for URI

aux = 0
for i in range(1,101):
    entrada = int(input())

    if (entrada > aux):
        aux = entrada
        posicao = i

print(aux)
print(posicao)
