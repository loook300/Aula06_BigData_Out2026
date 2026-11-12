venda = float (input('Valor da venda:  '))

match venda :
    case venda if venda <=100 :
        print ('Venda PEquena ')
    case venda if venda < 500 :
            print ('Venda Media')
    case _:
            print ('Venda Grande')