velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('Multado! voce excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade-80) * 7
    print('VocÊ deve pagar uma multa de R${:.2F}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')