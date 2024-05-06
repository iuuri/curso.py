"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""


numero = input('Vou dobrar o numero que vc digitar: ')

try:
    numero_int = int(numero)
    print(f'O dobro de {numero} é {numero_int * 2}')
except:
    ...

# if numero.isdigit():
#     numero_int = int(numero)
#     print(f'O dobro de {numero} é {numero_int * 2}')
# else:
#     print('Isso não é um número')