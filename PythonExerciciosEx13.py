salario = float(input('Qual é o salário do Funcionário? R$'))
novo = salario + (salario * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com aumento de 15% passa á receber R${:.2f}'.format(salario, novo))