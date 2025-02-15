'''
Escreva um programa que pergunte o salário do funcionário e
calcule o valor do aumento. Para salários superiores a R$ 1250,00
calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.
'''
print("")

salario = float(input("Digite seu salário: R$ "))
if salario > 1250:
    aumento = salario * 10 / 100
    novo_salario = salario + aumento
    print(f"Com 10% de aumento você receberá R$ {aumento:.2f} a mais. Seu salário agora será R$ {novo_salario:.2f}.")
if salario <= 1250:
    aumento = salario * 15 / 100
    novo_salario = salario + aumento
    print(f"Com 15% de aumento você receberá R$ {aumento:.2f} a mais. Seu salário agora será R$ {novo_salario:.2f}.")
