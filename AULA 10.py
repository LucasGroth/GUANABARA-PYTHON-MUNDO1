#Um programa que leia as médias bimetrais de um aluno, analise e diga se ele foi aprovado ou não.
from math import ceil
m1= float(input('Digite a nota do primeiro bimestre:'))
m2= float(input('Digite a nota do segundo bimestre:'))
m3= float(input('Digite a nota do terceiro bimestre:'))
m4= float(input('Digite a nota do quarto bimestre:'))
mediafinal=ceil(m1+m2+m3+m4)/4
if mediafinal>=7.0:
    print('Parabéns você foi aprovado! Sua média final foi {:.2f}!'.format(mediafinal))
else:
    print('Você não atingiu a média necessária para ser aprovado, sua média final foi {:.2f}!'.format(mediafinal))
