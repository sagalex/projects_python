""" aula 18
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range


volante = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']
#   (+)   0    1    2     3    4     5
lista = ['A', 'B' , 'C' ,'D' ,'E', 10.5]
#   (-)   6     5    4     3    2    1

l1 = [1, 2, 3]
l2 = [4, 5, 6, 7, 9]
l5 = [1, 2, 3, 4,  5, 6, 7, 8]

print(lista[-4])
print(lista[1])
print(lista[-1])
lista[3] = 'papai'
print(lista)
print(lista[0:3])
print(lista[0:5])
print(lista[::2])
print(lista[::-1])
print(l1)
print(l2)
l3 = l1 + l2
print(l3)
l1.extend(l2)
print(l1)
l1.extend('a')
print(l1)
l2.append('b')
print(l2)
l2.insert(0, 'banana')
print(l2)
l2.pop(-2)
print(l2)
del(l2[2:5])
print(l2)
print(max(l5))
print(min(l5))

l6 = list(range(1,101))
print(l6)

l10 = ["string", True, 10, -22.33]

for elemento in l10:
    print(f'O tipo de elemento é {type(elemento)} e seu valor é {elemento}')

#-------------------------------------------------------------------------------------
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)

fruits = ['apple', 'banana', 'cherry', 'banana']
x = fruits.index("banana")
print(x)
print(fruits[x])

for x in "banana":
  print(x)
"""

senha = 'perfume'
tm_senha= len(senha)
contador = 0
palavra = []
tentativas = []

print("Jogo de adivinhe a PALAVRA")

for x in range(tm_senha):
    palavra.append(x)

print(f'A palavra tem  {palavra} posições')

while True:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Isso não vale, digite uma letra.')
        continue

    if (letra in senha) and (letra != ''):
        print(f'Show! a letra: "{letra}" existe na palavra secreta!')

        for x in range(tm_senha):
          if letra == senha[x]:
            palavra[x] = senha[x]

        print(senha[x], palavra)


    else:
      print(f'Opa! A letra: {letra} não existe na Palavra')
      tentativas.append(letra)
      contador += 1
      print(f'Você tem {2 * tm_senha} chances! Você já errou {tentativas}, {contador} tentativa(s)')

      if contador >= (2 * tm_senha):
        print('Você perdeu!')
        break