"""
Formatando valores com modificadores
:s - texto (strings)
:d - inteiros (int)
:f - numeros de ponto flutuante (float)
:.(número)f - quantidade de casas decimais (float) :.2f
:(caractere) (> ou < ou ^) (quantidade) (tipo - s, d ou f)
> - a esquerda
< - a direita
^ - ao centro
"""
num_1 = 10
num_2 = 3
num_3 = 9999
num_4 = 88

nome = "Sergio Alexandre"
nome2 = 'Alex'
sobrenome1 = 'Guida'
sobrenome2 = 'Araujo'
divisao = num_1 / num_2



print('SAIDA DE DADOS')
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')


print(f'{nome:s}')
print()
print(f'{num_2:0>10}')
print(f'{num_3:0>10}')
print(f'{num_3:0<10}')
print(f'{num_3:0^10}')
print(f'{num_4:0>10.4f}')
print(f'{nome2:0>10}')
print()
print(len(nome))
print(len(nome2))
print()
nome_formatado = '{:*^20}'.format(nome2)
print(nome_formatado)
nome_formatado = '{n:#^20}'.format(n=nome2)
print(nome_formatado)
nome_formatado = '{0:*^20} {1:*^20} {2:*^20}'.format(nome, sobrenome1, sobrenome2)
print(nome_formatado)
print(nome.lower()) #tudo minusculo
print(nome.upper()) #tudo maiusculas
print(nome.title()) #primeiras letras maiusculas