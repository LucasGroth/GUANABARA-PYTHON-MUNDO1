#Um algoritmo que leia o salário de um funcionário, e mostre seu novo salário com aumento de 15%.
base=float(input('Digite o valor do salário atual: '))
aumento=0.15
novosalario=base*aumento+base
print('O funcionário que recebe R${}, se ganhar um aumento de 15%, passará a receber R${:.2f}'.format(base,novosalario))
