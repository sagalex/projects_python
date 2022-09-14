
nome = "Sergio Alexandre"  #string
idade = 54  # inteiro
altura = 1.70  # real ou ponto flutuante
valor = idade > 18  # valor booleano
peso = 88
imc = peso/(altura**2)
data_atual = 2022

print("Nome: ", nome)
print("idade: ", idade)
print("altura: ", altura)
print("Maior de idade: ", valor)
print(data_atual)

print(" O seu IMC = ", peso/(altura**2))
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))
print('{0} tem {1} anos de idade e seu imc é {1:.2f}'.format(nome, idade, imc))
print('{i} tem {n} anos de idade e seu imc é {im:.2f}'.format(n=nome, i=idade, im=imc))

nome = "Jason Miguel"  #string
idade = 51  # inteiro
altura = 1.76  # real ou ponto flutuante
peso = 77
Ano_nasc = 2022 - 51
imc = peso/(altura**2)

print(f'Nome: {nome} - Nacimento: {Ano_nasc} - idade: {idade} - altura: {altura} - Peso: {peso}Kg - IMC: {imc:.2f}')