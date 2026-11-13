


desconto = 0

for i in range (5) :
    venda = float (input ('Informe o Valor da venda: '))
    if venda < 200 :
        print ('Você nao tem desconto')

    elif venda  >= 200 :
        desconto = venda * 0.10 
        valor_total = venda - desconto
        print(f'Valor final da compra: {valor_total}R$ ')