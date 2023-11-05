

feminino = 62.1
altura = float(input('Informe sua altura em metros: '))
sexo = input('Informe seu sexo: ')
masculino = (72.7*altura)-58
feminino = (62.1*altura)-44.7
if sexo == masculino:
    print(f'Seu peso ideal é: {masculino:.2f}')
else:
    print(f'Seu peso ideal é: {feminino:.2f}')


# print(f'À área total e de {area:.2f}')
