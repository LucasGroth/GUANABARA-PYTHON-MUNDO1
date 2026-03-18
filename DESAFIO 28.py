#Um programa que faça o computador pensar em um número inteiro de 0 a 5 e peça para o usuário tentar descobrir qual é
# o número que ele pensou. O programa deverá dizer se o usuário errou ou acertou.
import random
start=input('Vamos começar? (S/N) ').strip().upper()
if start=='S':
    n= random.randint(0,5)
    print('Estou pensando em um número de 0 a 5, adivinhe qual é o número?')
    resposta=int(input())
    if resposta == n:
        print('Parabéns, você adivinhou!')
    else:
        print('Você errou, o número que eu estava pensando era o número {}!'.format(n))
else:
    print('Tudo bem então!')

#DESAFIO PESSOAL, CRIAR UM SISTEMA DE VIDAS, EM QUE O JOGADOR PERDE UMA VIDA CADA VEZ QUE ERRA O PALPITE DO NUMERO
#ADICIONAR AO FINAL BOTÃO DE REPLAY.