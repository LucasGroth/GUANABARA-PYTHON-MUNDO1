#Um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m=float(input('Digite em metros a distancia que você correu hoje:'))
cm= m*100
mm= m*1000
km= float(m/1000)
hm= float(m/100)
dm= float(m/10)
dcm= m*10
print('Você correu {} metros,em centímetros você correu {}cm e em milímetros você correu {}mm'.format(m,cm,mm))
print('Em km isso representa {:.2f}km, em hectonetro {:.2f} hm, em decametro {:.2f}dm e em decimetros {:.2f}dcm'.format(km,hm,dm,dcm))
