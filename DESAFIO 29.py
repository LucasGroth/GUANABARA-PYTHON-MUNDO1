#Um programa que leia a velocidade de um carro. Se ele ultrapassar 80 Km/h, mostre uma mensagem informando que ele foi
# multado, a multa vai custar R$07,00 por Km/h  acima do limite permitido.
velocidade=int(input('Informe qual era a velocidade do seu veículo:'))
multa=int((velocidade-80)*7.0)
if velocidade>80:
    print('Você foi multado por excesso de velocidade!')
    print('O valor da multa é de R$ {:.2f}'.format(multa))
else:
    print('Você estava dentro do limite de velocidade e nenhuma multa foi aplicada.')