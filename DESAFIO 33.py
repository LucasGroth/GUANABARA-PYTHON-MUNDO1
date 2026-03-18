#Um programa que leia três número e mostre qual é o maior e qual é o menor
n1=int(input('Informe o primeiro numero inteiro:'))
n2=int(input('Informe o segundo numero inteiro:'))
n3=int(input('Informe o terceiro numero inteiro:'))
#calcular n1
print('Analisando números informados, aguarde.')
if n1<n2:
    if n1<n3:
        print('{} é o menor número'.format(n1))
    else:
        print('{} é o menor número'.format(n3))
else:
    if n2<n3:
        print('{} é o menor número'.format(n2))
if n1 > n2:
    if n1 > n3:
        print('{} é o maior número'.format(n1))
    else:
        print('{} é o maior número'.format(n3))
else:
    if n2 > n3:
        print('{} é o maior número'.format(n2))
