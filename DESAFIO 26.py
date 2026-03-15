#Um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra a
#Onde ela aparece a primeira vez
#Em que posição ela aparece pela ultima vez
frase=input('Digite uma frase:').strip().lower()
print('Na frase a letra "a" aparece {} vezes.'.format(frase.count('a')))
print('A letra A aparece pela primeira vez na posição {}.'.format(frase.find('a')+1))
print('A letra "a" aparece pela ultima vez na frase na posição {}.'.format(frase.rfind('a')+1))
print('A frase tem {} posições.'.format(frase.count('')-1))
