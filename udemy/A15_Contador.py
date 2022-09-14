contador = -9
acumulador = 0
while contador <=9:
    contador += 1
    acumulador = acumulador + contador
    print(contador, acumulador)
    if contador > 5:
        continue
else:
    print('cheguei no else')

