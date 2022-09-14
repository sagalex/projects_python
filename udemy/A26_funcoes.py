# exercício 1
def mensagemg_tela(msg='Hello', nome='user'):
        print(msg, nome)

mensagemg_tela('Faaaaaala!', "Sergio")

# exercício 2
def soma_tres(a1, a2, a3):
    soma = a1 + a2 + a3
    print(soma)
soma_tres(23, 33, 53)

# exercício 3
def porcentagem(valor, xp):
    xp = xp/100
    return valor + (valor * xp)
print(porcentagem(15,100))

# exercício 4
def FizzBuzz_C(num):
    if num % 3 == 0 and num % 5 == 0:
        return f'FizzBuzz, {num} é divisível por 3 e 5'
    if num % 5 == 0:
        return f'Buzz, {num} é divisível por 5'
    if num % 3 == 0:
        return f'Fizz, {num} é divisível por 3'
    return num

from random import randint

for i in range(100):
    aleatorio = randint(0, 100)
    print(FizzBuzz_C(aleatorio))


def FizzBuzz(num):
    if not num % 3:
        Fizz = 'OK'
    else:
        Fizz = 'NO3'

    if not num % 5:
        Buzz = 'OK'
    else:
        Buzz = 'NO5'

    if Fizz == Buzz:
        return 'FizzBuzz'
    elif Fizz == 'OK':
        return 'Fizz'
    elif Buzz == 'OK':
        return 'Buzz'
    else:
        return num

print(FizzBuzz_C(5))













