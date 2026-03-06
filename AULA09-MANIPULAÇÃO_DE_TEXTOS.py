#Manipulação de textos
from random import shuffle, choice
frase='Aprendendo manipulação de textos'
ordemsplit=frase.split()
print('A frase é "{}".'.format(frase))
print('A quarta letra é "{}".'.format(frase[3]))
print('Se escrevermos da primeira à décima posição teremos : {}'.format(frase[:11]))
print('Pulando de um em um teremos: "{}.'.format(frase[::2]))
print('Na frase temos {} micro espaços utilizados.'.format(len(frase)))
print('Na frase temos {} "a"!'.format(frase.count('a')))
print('Na frase temos as palavras: {}'.format(frase.split()))
print('Palavra aleatória escolhida: {}'.format(choice(ordemsplit)))
print('Sendo a primeira "{}", a segunda "{}", a terceira "{}" e a quarta "{}".'.format(ordemsplit[0],ordemsplit[1],ordemsplit[2],ordemsplit[3]))
print('Primeira palavra sem embaralhar : {}'.format(frase[0]))
shuffle(ordemsplit)
print('A primeira palavra depois do comando shuffle(ordemsplit): {}.'.format(ordemsplit[0]))
print('Encontramos a palavra de na posição {}'.format(frase[6:].find("de")))
#AQUI PRECISEI EDITAR O VALOR DO COMEÇO DA ANÁLISE PQ "DE" EXISTE NA PALAVRA APRENDENDO,
#PORÉM DESSA MANEIRA OS VALORES DOS ESPAÇOS MUDAM E A POSIÇÃO 24 PASSA A SER 17.
#PRECISO PROCURAR UMA MANEIRA MELHOR DE FAZER ESSA LOCALIZAÇÃO.
print('Embaralhando a ordem poderia ficar: {}'.format(ordemsplit))
print('usando o módulo replace com a palavra "python", teremos:{}.'.format(frase.replace('textos','python')))
print('------------------------------------------------------------------------------------------------------')
titulo='Como manipular textos?'
print(titulo.upper())
print(titulo.lower())
print(titulo.title())
print(titulo.center(100))
