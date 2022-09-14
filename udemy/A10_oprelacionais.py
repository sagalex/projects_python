"""
Operadores Relacionais
== > >= =< < !=
"""

print(2=='2')  #falso

num_1 = 9 #int
num_2 = 2 #int

expressao = num_1 != num_2

print(expressao)

nome = input("Qual o seu nome? ")
idade = int(input('Qual a sua idade? '))

idade_limite = 18
idade_menor = 20
idade_maior = 30

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} Não pode pegar o empréstimo.')