x = int(input(''))
y = int(input(''))

# comparação do menor
if (x < y) or (x == y):
    x = x
    y = y
    
if (x > y):
    aux = x
    x = y
    y = aux

# criando lista do valor x ate o valor y
lista_total = []
x = x + 1           #tira o x da contagem, começando do proximo numero mais alto.
for cont in range(x,y):
    lista_total.append(cont)            #ate aqui gerou uma lista com todos os valores entre x e y, tirando eles mesmos.


# insere os apenas os valores impares na lista_impar
lista_impar = []
for cont in lista_total:
    if(cont % 2 != 0):
        lista_impar.append(cont)

soma = sum(lista_impar)     #somando todos os valores impares
print('{}'.format(soma))
