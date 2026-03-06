#Um programa que leia um angulo qualquer e mostre na tela o valor  do seno, cosseno e da tangente desse ângulo.
from math import sin, cos, radians, tan
angulo = float(input('Digite um angulo qualquer:'))
seno= sin(radians(angulo))
cosseno= cos(radians(angulo))
tangente= tan(radians(angulo))
print('O angulo {} tem valor de seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(angulo,seno,cosseno,tangente))
