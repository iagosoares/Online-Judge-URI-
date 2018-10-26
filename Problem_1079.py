n = int(input())

lista = []

while n!= 0:
    a,b,c = input().split()
    
    lista.append((float(a)*0.2) + (float(b)*0.3) + (float(c)*0.5))
    n = n - 1

for cont in lista:
    print("{:0.1f}".format(cont))
