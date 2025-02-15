'''
Escreva um programa que leie o salário de um funcionário, calcule e imprima o
salário com um aumento de 15%.
'''
print("")

salario = float(input("Digite o salário do funcionário: R$ "))
print(f"Salário convencional: R$ {salario:.2f}")
salario_aumento = salario + (salario * 15/100)
print(f"Com 15% de aumento seu salário será R$ {salario_aumento:.2f}")
