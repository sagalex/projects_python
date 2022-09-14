"""

numero = input("Digite um número inteiro: ")

if numero.isdigit():
    numero = int(numero)
    if (int(numero) % 2) == 0:
        print(f'O {numero} é par')
    else:
        print(f'O {numero} é impar')
else:
    print('Isso não é um número inteiro')


horario = input("Digite um horário (0 - 23): ")
if horario.isdigit():
    horario = int(horario)
    if horario < 0 or horario > 23:
        print(" O horário deve estar entre 0 e 23")
    else:
        if horario < 11:
            print('Bom dia!')
        elif horario <= 17:
            print('Boa tarde!')
        else:
            print('Boa noite')

else:
    print("Por favor digite um horário entre 0 e 24.")

"""
nome = input('Digite o seu nome: ')
tamanho = len(nome)

if tamanho <=4:
    print('Seu nome é curto!')
elif tamanho <=6:
    print('Seu nome é normal!')
else:
    print('Seu nome é muito grande')