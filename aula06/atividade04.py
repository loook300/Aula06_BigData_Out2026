




for i in range (5) :
    venda = float (input ('\nInforme o Valor da Compra: '))
    if venda >= 200 :
        desconto = venda * 0.10
        

    else:
        desconto = 0 

    valor_total = venda - desconto
    print(f'\nDesconto de R$: {desconto}R$ ')
    print(f'Valor final da compra: {valor_total}R$ ')
