import math
i = 0
j = 1

for cont1 in range(11):
    i = round(i,2)
    j = round(j,2)
    
    if i == 1.0:
        i = math.trunc(i)
    elif i == 2.0:
        i = math.trunc(i)
        
    if j == 2.0:
        j = math.trunc(j)
    elif j == 3.0:
        j = math.trunc(j)
    elif j == 4.0:
        j = math.trunc(j)

    for cont2 in range(3):
        print("I={} J={}".format(round(i,2),round(j,2)))
        j = j + 1
    aux = j - 2.8
    j = aux
    i += 0.2 
