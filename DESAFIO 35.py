#Um programa que leia o comprimento de três retas e diga ao usuário
# se elas podem ou não formar um triângulo.
#Somar as duas menores retas e a soma delas tem que ser maior que a maior reta. (usaremos 3,4 e 5)
ra=int(input('Informe o tamanho da primeira reta:'))
rb=int(input('Informe o tamanho da segunda reta:'))
rc=int(input('Informe o tamanho da terceira reta'))
#primeiro vamos descobrir qual a maior reta e quais as menores.
menor=ra
if rb<ra and rb<rc:
    menor=rb
if rc<ra and rc<rb:
    menor=rc
#Agora calculamos o maior
maior=ra
if rb>ra and rb>rc:
    maior=rb
if rc>ra and rc>rb:
    maior=rc
#Agora precisamos fazer o computador identificar o segundo menor número
segundo=ra
if rb<ra and rb>rc:
    segundo=rb
if rc<ra and rc>rb:
    segundo=rc
#Agora o computador deve calcular as retas e verificar a condição de existencia de triangulo.
if menor+segundo>maior:
    print('Com essas retas informadas é possível sim formar um triangulo')
else:
    print('Com essas retas informadas não é possível formar um triangulo')
#METODO  DO GUANABARA KKKKKK Muito mais simples
if ra<rb + rc and rb<ra + rc and rc<ra + rb:
    print('Forma triangulo')
else:
    print('Não forma triangulo')