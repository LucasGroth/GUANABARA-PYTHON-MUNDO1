##Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele
dadoanalisado=input('Digite algo:')
tipo= type(dadoanalisado)
print('Analise de dado informado:')
print('{} é do tipo {} '.format(dadoanalisado,tipo))
print('{} é um número?'.format(dadoanalisado),dadoanalisado.isnumeric())
print('{} é alfabético?'.format(dadoanalisado),dadoanalisado.isalpha())
print('{} é alfanumérico?'.format(dadoanalisado),dadoanalisado.isalnum())
print('{} é decimal?'.format(dadoanalisado),dadoanalisado.isdecimal())
print('{} está todo em minúsculo?'.format(dadoanalisado),dadoanalisado.islower())
print('{} está todo em maiúsculo?'.format(dadoanalisado), dadoanalisado.isupper())
print('{} só tem espaço?'.format(dadoanalisado),dadoanalisado.isspace())
print('{} só tem caracteres ASCII?'.format(dadoanalisado), dadoanalisado.isascii())
print('{} é digito?'.format(dadoanalisado),dadoanalisado.isdigit())
print('{} é uma palavra reservada de python?'.format(dadoanalisado),dadoanalisado.isidentifier())
print('{} é printável?'.format(dadoanalisado),dadoanalisado.isprintable())
print('{} está em formato de titlecase?'.format(dadoanalisado),dadoanalisado.istitle())
## Fazer mesmo exercício posteriormente com estruturas de if.
## Para esse desafio, procurei o que era cada. is na documentaçaõ do python para saber o que significava cada um.