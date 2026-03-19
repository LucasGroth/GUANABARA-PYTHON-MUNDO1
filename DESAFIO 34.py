#Um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários acima de 1250 calcule um aumento de 10%.
#Para inferiores ou iguais o aumento será de 15%.
salario=float(input('Informe o salário do funcionário:'))
if salario <= 1250.00:
    print('O novo salário do funcionário pós aumento de 15% será de R${:.2f}.'.format(salario + (salario*0.15)))
else:
    print('O novo salário do funcionário pós aumento de 10% será de R${:.2f}.'.format(salario*0.10+salario))