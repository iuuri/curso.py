# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1

# nome = 'Iuri'
# print(nome[2])
# print(nome[-2])
# print('r' in nome)
# print('s' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} existe em {nome}')
else:
    print(f'{encontrar} não existe em {nome}')

