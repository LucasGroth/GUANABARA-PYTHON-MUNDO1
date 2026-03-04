#Um programa que leia quanto você tem em R$ na carteira e informe quanto vale isso em outras moedas
real=float(input('Quantos reais você tem?'))
vdolar=5.22
veuro=6.08
vlibra=6.98
vpesoarg=0.0037
print('Segue tabela de R${:.2f} convertido em outras moedas:'.format(real))
print('Valor em dólar = {:.2f}'.format(real/vdolar))
print('Valor em euros = {:.2f}'.format(real/veuro))
print('Valor em libras esterlinas = {:.2f}'.format(real/vlibra))
print('Valor em pesos argentinos = {:.2f}'.format(real/vpesoarg))
## DESAFIO PESSOAL - FAZER PROGRAMA COM ESTRUTURA DE IF.
##Onde o programa recebe o valor recebe qual moeda base, recebe qual a moeda final e o valor a ser convertido.
##Como o conversor de moedas do Google.

