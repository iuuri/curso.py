nome = 'Iuri Souza'
altura = 1.79
peso = 79
imc = peso / (altura * altura)


#f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'


print(linha_1)
print(linha_2)
print(linha_3)

print(nome, 'tem', altura, 'de altura', ', pesa', peso, 'quilos', 'e seu imc é:' , imc )