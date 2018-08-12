entrada = int(input())

valor = entrada

i = 0
j = 0
l = 0
m = 0
n = 0
p = 0
t = 0 

while(valor >= 100):
   valor = (valor - 100)
   i = i + 1

while(valor >= 50):
   valor = (valor - 50)
   j = j +1

while(valor >= 20):
   valor = (valor - 20)
   l=l+1

while(valor >= 10):
   valor = (valor - 10)
   m=m+1
while(valor >= 5):
   valor = (valor - 5)
   n=n+1

while(valor >= 2):
   valor = (valor - 2)
   p=p+1

while(valor >= 1):
   valor = (valor - 1)
   t=t+1

print(entrada)
print(i,"nota(s) de R$ 100,00")
print(j,"nota(s) de R$ 50,00")
print(l,"nota(s) de R$ 20,00")
print(m,"nota(s) de R$ 10,00")
print(n,"nota(s) de R$ 5,00")
print(p,"nota(s) de R$ 2,00")
print(t,"nota(s) de R$ 1,00")
