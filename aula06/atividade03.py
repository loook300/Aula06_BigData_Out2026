 ##digite = int(input('Digite um Numero: '))


#dobro = digite *2
# tripulo = digite *3
# quadrado = digite ** 2

# print(f'''
# [Dobro]    : {dobro}
# [Tripulo]  : {tripulo}
# [Quadrado] : {quadrado}
# ''')

for i in range(3):
    print(f'\n RODADA {i +1}')
    digite = int(input('Digite um Numero: '))

    dobro = digite *2
    tripulo = digite *3
    quadrado = digite ** 2

    print(f'''
    [Dobro]    : {dobro}
    [Tripulo]  : {tripulo}
    [Quadrado] : {quadrado}
    ''')