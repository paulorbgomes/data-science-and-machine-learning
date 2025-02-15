'''
Faça um programa que calcule o aumento de um salário. Ele deve
solicitar o valor do salário e a porcentagem de aumento. Exiba
o valor do aumento e do novo salário.
'''
print("")

salario = float(input("Informe o salário: R$ "))
porcentagem = float(input("Informe a porcentagem de aumento: "))

print(f"Salário sem aumento: R$ {salario:.2f}")
aumento = salario * porcentagem / 100
novo_salario = salario + aumento
print(f"Seu aumento será de R$ {aumento:.2f}")
print(f"Seu novo salário será R$ {novo_salario:.2f}")

