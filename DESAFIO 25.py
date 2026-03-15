#Um programa que leia o nome de uma pessoa e diga se tem o nome "silva" no nome
nome=input('Qual o seu nome?').strip()
nome=nome.lower()
separado=nome.split()
if separado.__contains__('silva'):
#Ou posso usar: if 'silva' in separado:
    print('Seu nome tem silva')
else:
    print('Seu nome não tem silva')