valor = float (input('Valor da Venda: '))

print('''

[1] - Pix (12% de Desconto)
[2] - Débito (8% de Desconto)
[3] - Crédito (5% de Desconto)
[4] - Dinheiro (15% de Desconto)


''')
#true 
desconto = 0 
opcao = int (input('Informe a opção Escolhida:  '))


match opcao :
    case 1 :
        print('----Pix----')
        desconto = valor * 0.12
    case 2 :
            print('----Debito----')
            desconto = valor * 0.08
    case 3 :
            print('----Credito----')
            desconto = valor * 0.05
    case 4 :
            print('----Dinheiro----')
            desconto = valor * 0.15
    case _ :
            print('----Opção Invalida----')
#if operacao == true :
#if opcao in [1, 2, 3, 4]:
if desconto !=0 :
       valor_final = valor - desconto
       print(f'Preço : {valor}')
       print(f'Desconto : {desconto}')
       print(f'Total a pagar : {valor_final}')
else:
       print('Por favor,escolha uma das opções acima')