from random import randint
from time import sleep
computador = randint(0, 5)  #faz o computador sortear
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('Processando um número...')
sleep(2)
if jogador == computador:
    print('Parabens! Voce conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))