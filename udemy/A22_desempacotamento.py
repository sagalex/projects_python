"""
Desempacotamento
O * antes do nome define um lista no meio das variáveis

"""
lista = ['Luiz', 'João', 'Maria', 1,2,3,4,5,6,7,8,9,100]

n1, n2, n3, *outra_lista, antipenultimo_valor, ultimo_valor = lista
print(n1, n2, n3, outra_lista, antipenultimo_valor, ultimo_valor)


n1, n2, *_ = lista # *_ diz que os outros valores não são necessários.
print(n1, n2)