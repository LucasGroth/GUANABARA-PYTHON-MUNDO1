#Um programa que leia o comprimento do cateto oposto e do cateto adjacente de uma triangulo retangulo, calcule e mostre a hipotenusa
from math import pow,sqrt,hypot
catetoa=float(input('Digite o valor do cateto adjacente'))
catetoo=float(input('Digite o valor do cateto oposto'))
h=sqrt(pow(catetoa,2)+pow(catetoo,2))
#utilizando modulo hypot
hi=hypot(catetoa,catetoo)
print('A hipotenusa vai medir {:.2f}'.format(h))
print('A hipotenusa vai medir {:.2f}'.format(hi))
