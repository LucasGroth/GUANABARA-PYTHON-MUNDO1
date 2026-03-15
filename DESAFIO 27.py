#Um programa que leia o nome completo de uma pessoa e mostre separadamente o primeiro e o ultimo nome
nome=input('Qual o seu nome?').strip()
primeironome=nome.split()[0]
ultimonome=nome.split()[-1]
print('Seu primeiro nome é {}.'.format(primeironome))
print('Seu ultimo nome é {}.'.format(ultimonome))
