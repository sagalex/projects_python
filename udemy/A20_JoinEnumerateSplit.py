string = "O Brasil é o o o pais do futebol, o Brasil é penta"
lista_1 = string.split(' ')
lista_2 = string.split(',')
lista_A = [1, 2, 6, 9, 3, 6, 4]
print (lista_1)
print (lista_2)

lista_3 = ' '.join(lista_1)
print(lista_3)

palavra = ''
contagem = 0


for valor in lista_2:
    print(valor.strip().capitalize())
"""
for valor in lista_1:
    #print(f'A palavra {valor} apareceu {lista_1.count(valor) x na frase}')
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')
"""

