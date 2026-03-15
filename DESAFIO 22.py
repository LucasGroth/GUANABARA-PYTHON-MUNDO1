#Um programa  que leia o nome do usuário e mostre, com todas a letras maiúsculas, todas minusculas, quantas letras ao
#todo, quantas letras sem contar espaço
nome=input('Digite o seu nome:').strip()
print(nome.upper())
print(nome.lower())
print('Sem contar os espaços, seu nome tem {} letras.'.format(len(nome)-nome.count(' ')))
fatia=(nome.split())
print('O seu primeiro nome tem {} letras.'.format(len(fatia[0])))
