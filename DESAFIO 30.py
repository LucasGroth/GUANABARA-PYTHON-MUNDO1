#Um programa que leia um número inteiro e diga se ela é par ou impar
n=int(input('Informe um número inteiro qualquer e eu vou dizer se é par ou impar. Pode digitar:'))
if n%2==0:
    print('{} é um número par!'.format(n))
else:
    print('{} é um número impar!'.format(n))