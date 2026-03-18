#Um programa que leia um ano qualquer e diga se ele é bissexto.
ano=int(input('Digite um ano qualquer e eu digo se é bissexto ou não; Pode digitar:'))
if ano%4==0:
    if ano%100==0:
        if ano%400==0:
            print('{} é um ano bissexto!'.format(ano))
        else:
            print('{} não é um ano bissexto, pois não é divisível por 400!'.format(ano))
    else:
        print('{} é um ano bissexto, pois é divisel por 4 mas não por 100!'.format(ano))
else:
    print('{} não é um ano bissexto, pois não é divisível por 4!'.format(ano))
