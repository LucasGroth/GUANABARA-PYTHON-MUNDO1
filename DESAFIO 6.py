#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n=float(input('Digite um numero inteiro:'))
dobro=n*2
triplo=n*3
raiz=n**(1/2)
print('O numero digitado foi {}, o dobro disso é {}, o triplo é {} e sua raiz quadrada é {}'.format(n,dobro,triplo,raiz))
#Utilizei float na variavel n,pois, no enunciado não deixava explicito que seria número inteiro, logo tinha margem para trabalhar com números decimais.