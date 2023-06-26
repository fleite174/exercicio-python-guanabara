dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodadas? '))
pago = (dias * 60) + (km * 0.15)
print('O total apagar é de R${:.2F}'.format(pago))