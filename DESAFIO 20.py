#Um programa que sorteie a ordem de apresentação de grupos da sua turma.
from random import shuffle
g1=input('Digite o nome do primeiro grupo')
g2=input('Digite o nome do segundo grupo')
g3=input('Digite o nome do terceiro grupo')
g4=input('Digite o nome do quarto grupo')
lista=[g1,g2,g3,g4]
shuffle(lista)
print('A ordem das apresentações será, {}'.format(lista))
