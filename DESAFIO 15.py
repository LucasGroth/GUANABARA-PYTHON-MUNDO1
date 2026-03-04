#Um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais
#ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 POR kM rodado. .formart(dias,km,(precokm+precodias)))
km=int(input('Quantos Kms foram percorridos?'))
dias=int(input('Quantos dias que o carro foi alugado?'))
precokm=km*0.15
precodias=dias*60
print('O carro foi alugado por {} dias e percorreu {} quilômetros, então no total a locação custou R${:.2f} !'.format(dias,km,(precokm+precodias)),'\n''R${:.2f} pelos dias de aluguel e R${:.2f} pela quilometragem percorrida'.format(precodias,precokm))