#Um programa que pergunte a distancia de uma viagem em Km.
#Calcule o preço da passagem, cobrando 0,50 por km em viagens de até 200Km
#Para viagens acima de 200Km 0,45 por km.
distancia=int(input('Informe a distancia da viagem em quilômetros: '))
if distancia<=200:
    viagemcurta=distancia*0.50
    print('O preço da passagem para sua viagem é de R$ {}'.format(viagemcurta))
else:
    viagemlonga=distancia*0.45
    print('O preço da passagem para sua viagem é de R$ {}'.format(viagemlonga))