def main(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def tx_1(nome):
    return f'O nome é: {nome}'

def tx_2(nome,saudacao):
    return f'{saudacao}, {nome}'

executando = main(tx_1, 'Sergio')
executando2 = main(tx_2,'Alexandre', saudacao='Bom dia')
print(executando)
print(executando2)


