#-------------Invertendo valores------------------------------------
x = 10
y = 'Sergio'
z = 'SAGA'
(x, y) = (y, x)

print(f'x={x} e y={y}')
x, y, z = z, x, y
print(f'x={x} e y={y} e z={z}')
#-------------------------------------------------
"""
Operador ternário em Python: são testes tão simples 
que  retorna um valor para apenas duas possibilidades.
"""
logged_user = False

if logged_user:
    msg ='Usuário logado'
#-------------------------------------------------
nome = input('Qual o seu nome?')
print(nome or 'Você não digitou nada!')
#-------------------------------------------------
a = 0 # retorna um valor falso
b = None # retorna um valor falso
c = False # retorna um valor falso
d = [] # retorna um valor falso
c = {} # retorna um valor falso
d = 22 # retorna um valor verdadeiro
e = 'Sergio' # retorna um valor verdadeiro


variavel = a or b or c or d or e # para na primeira verdadeira da esquerda para a direita.

print(variavel)