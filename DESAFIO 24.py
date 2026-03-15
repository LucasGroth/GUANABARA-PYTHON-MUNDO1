#Um programa que leia o nome da sua cidade e diga se ela começa ou não com a palavra "Santo"
cidade=input('Digite o nome da cidade: ').strip()
leitura=cidade.lower()
leitura.split(' ')
primeironome=leitura.split()[0]
if primeironome == 'santo':
    print('Sua cidade começa com a palavra santo')
else:
    print('Sua cidade não começa com a palavra santo')