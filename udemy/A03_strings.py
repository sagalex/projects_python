"""
Manipulando strings
*String indices
fatiamento de strings [inicio:fim:passo]
funções built-in, le, abs, type, print, etc...
"""
# indices +    012345678
texto       = "Python s2"
# indices -    987654321
print(texto[8])
print(texto[6])
print(texto[5])
print(texto[-1]) # imprime o indice -1 que é o último da string
print(texto[2:6]) # string[inicio:fim:passo]
print(texto[:6]) # irá imprimir os 6 primeiro caracteres suprimindo o início
print(texto[7:9]) # note que eu digitei um numero superior ao maior indice positivo
print(texto[0::2]) # aqui ele irá pegar do 0 até o 8 pulando de 2 em 2
print(texto[0:6:3]) # ele imprie do primeiro ao sexto caractere de 3 em 3

for letra in texto:
    print(letra)