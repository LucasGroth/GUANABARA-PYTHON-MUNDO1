#Um algoritmo que  leia o preço de um produto, aplique um desconto de 5% e mostre o novo valor
n=float(input('Informe o valor do produto: '))
desconto=n*0.05
vf=n-desconto
print('O produto que custava R${:.2f}, com desconto de 5%, agora custa R${:.2f}!'.format(n,vf))
#FAZENDO CALCULADORA DE DESCONTOS
a=float(input('Informe o valor do produto: '))
porcentagem=int(input('Informe o valor do desconto: '))
descdecimal=porcentagem/100
valorfinal=a-a*descdecimal
print('O produto que custava R${:.2f}, com {}% de desconto, agora custa R${:.2f} !'.format(a,porcentagem,valorfinal))
