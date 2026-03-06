#Um programa para sortear um aluno para ajudar o professor naquele dia.
from random import choice
aluno1= str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))
lista=[aluno1,aluno2,aluno3,aluno4]
sorteio= choice (lista)
print('O aluno sorteado de hoje é {}'.format(sorteio))
