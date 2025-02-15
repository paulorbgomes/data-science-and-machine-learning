'''
Escreva um programa para determinar se uma pessoa deve ou não
pagar imposto. Considere que pagam imposto pessoas cujo salário
é maior que R$ 1200,00.
'''
print("")

salario = float(input("Por favor, digite o seu salário: R$ "))
if salario > 1200:
    print(f"Seu salário é maior que R$ 1200,00. Você pagará imposto!")
else:
    print(f"Seu salário é menor que R$ 1200,00. Você não pagará imposto.")
