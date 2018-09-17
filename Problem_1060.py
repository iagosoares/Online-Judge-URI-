e1 = float(input())
e2 = float(input())
e3 = float(input())
e4 = float(input())
e5 = float(input())
e6 = float(input())
entrada = [e1, e2, e3, e4, e5, e6]
i = 0

for n in entrada:
    if (n > 0):
        i = i + 1

print('{} valores positivos'.format(i))
