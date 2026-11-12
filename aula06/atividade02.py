valor = float (input('Valor do Ingresso: '))

print('''

[1] - Inteira (Sem Desconto)
[2] - Meia Entrada (50% de Desconto)
[3] - Promoção (30% de Desconto)


''')

desconto = 0 
opcao = int (input('Informe a opção Escolhida:  '))


match opcao :
    case 1 :
        print('----Sem Desconto----')
    case 2 :
        print('----Meia Entrada----')
        desconto = valor * 0.50
    case 3 :
        print('----Promoção----')
        desconto = valor * 0.30

if opcao in [1, 2, 3]:
#if desconto !=0 :
      
    valor_final = valor - desconto
    print(f'Preço : {valor}')
    print(f'Desconto : {desconto}')
    print(f'Total a pagar : {valor_final}')
else:
    print('Opção invalida ')