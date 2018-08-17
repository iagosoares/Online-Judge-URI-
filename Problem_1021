import math

entrada = float(input())

ncem, ncinquenta, nvinte, ndez, ncinco, ndois = 0, 0, 0, 0, 0, 0

mum, mcinquenta, mvintecinco, mdez, mzerocinco, mzeroum = 0, 0, 0, 0, 0, 0

if entrada >= 0 and entrada <= 1000000.00:

		#NOTAS
			while entrada >= 100.00:
				entrada = entrada - 100.00
				entrada = float("%.2f" % entrada)
				ncem += 1				

			while entrada >= 50.00:
				entrada = entrada - 50.00
				entrada = float("%.2f" % entrada)
				ncinquenta += 1

			while entrada >= 20.00:
				entrada = entrada - 20.00
				entrada = float("%.2f" % entrada)
				nvinte += 1
				
			while entrada >= 10.00:
				entrada = entrada - 10.00
				entrada = float("%.2f" % entrada)
				ndez += 1

			while entrada >= 5.00:
				entrada = entrada - 5.00
				entrada = float("%.2f" % entrada)
				ncinco += 1

			while entrada >= 2.00:
				entrada = entrada - 2.00
				entrada = float("%.2f" % entrada)
				ndois += 1

#MOEDAS

while entrada >= 1.00:
	entrada = (entrada - 1.00)
	entrada = float("%.2f" % entrada)
	mum += 1

while entrada >= 0.50:
	entrada = (entrada - 0.50)
	entrada = float("%.2f" % entrada)
	round(entrada,2)
	mcinquenta += 1

while entrada >= 0.25:
	entrada = (entrada - 0.25)
	entrada = float("%.2f" % entrada)
	mvintecinco += 1

while entrada >= 0.1:
	entrada = (entrada - 0.1)
	entrada = float("%.2f" % entrada)
	mdez += 1

while entrada >= 0.05:
	entrada = (entrada - 0.05)
	entrada = float("%.2f" % entrada)
	mzerocinco += 1

while entrada >= 0.01:
	entrada = (entrada - 0.01)
	entrada = float("%.2f" % entrada)
	mzeroum += 1

print("NOTAS:")
print(ncem,"nota(s) de R$ 100.00")
print(ncinquenta,"nota(s) de R$ 50.00")
print(nvinte,"nota(s) de R$ 20.00")
print(ndez,"nota(s) de R$ 10.00")
print(ncinco,"nota(s) de R$ 5.00")
print(ndois,"nota(s) de R$ 2.00")
print("MOEDAS:")
print(mum,"moeda(s) de R$ 1.00")
print(mcinquenta,"moeda(s) de R$ 0.50")
print(mvintecinco,"moeda(s) de R$ 0.25")
print(mdez,"moeda(s) de R$ 0.10")
print(mzerocinco,"moeda(s) de R$ 0.05")
print(mzeroum,"moeda(s) de R$ 0.01")
