entrada = float(input())

if(entrada > 4500.00):
    imposto = ((entrada - 4500.00) * 0.28) + 350.00
    print('R$ {:.2f}' .format(imposto))

if(entrada > 3000.00 and entrada <= 4500.00):
    imposto = ((entrada - 3000.00) * 0.18) + 80.00
    print('R$ {:.2f}' .format(imposto))

if(entrada > 2000.00 and entrada <= 3000.00):
    imposto = ((entrada - 2000.00) * 0.08)
    print('R$ {:.2f}' .format(imposto))
    
if(entrada <= 2000.00):
    print('Isento')
