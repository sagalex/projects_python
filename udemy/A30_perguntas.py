print('--- QUESTIONÁRIO ---')
perguntas = {
    'Pergunta 1':{
        'pergunta':'Quanto é 2 + 2 ?',
        'respostas':{'a': '1','b': '4','c': '5'},
        'resposta_certa': 'b',
    },
    'Pergunta 2':{
        'pergunta':'Quanto é 3 * 2 ?',
        'respostas':{'a': '1','b': '40','c': '6'},
        'resposta_certa': 'c',
    },
}

resposta_certa = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    print('Respostas:')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')
    resposta_usuario = input('Sua resposta: ')
    if resposta_usuario == pv['resposta_certa']:    
        print('Eba! Ehhhhh! Você acertou!')
        resposta_certa += 1
    else:
        print('Ixiiiii!!! Você ERROU!')

qtd_perguntas = len(perguntas)
porcertagem_acerto = resposta_certa /qtd_perguntas * 100
print(f'Você acertou {resposta_certa} respostas')
print(f'Sua porcentagem de acreto foi de: {porcertagem_acerto}%')