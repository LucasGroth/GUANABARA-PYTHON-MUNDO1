#Programa que leia largura e altura de uma parede em metros, calcule sua área e quantidade de tinta para
# pintar essa parede, sendo que 1 litro de tinta pinta 2m².
altura=float(input('Qual a altura da parede em metros: '))
largura=float(input('Qual a largura da parede em metros: '))
area = altura*largura
tinta = area/2
print('A parede tem {}m² de área, e para pintá-la você precisará de {} litros de tinta'.format(area,tinta))
#Desafio pessoal - calcular se ele precisa comprar uma lata de tinta grande ou pequena, e quanto de cada uma.