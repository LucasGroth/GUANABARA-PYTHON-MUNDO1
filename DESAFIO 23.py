#Um programa que leia um numero inteiro de 0 a 9999 e mostre na tela cada um dos digitos separados
numero=int(input('Digite um numero de 0 a 9999: '))
milhar=numero //1000 % 10
centensa=numero //100 % 10
dezena=numero //10 % 10
unidade=numero // 1 % 10
print('O número informado contém {} milhas, {} centenas, {} dezenas e {} unidades.'.format(milhar,centensa,dezena,unidade))