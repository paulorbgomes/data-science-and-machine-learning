'''
Escreva um programa que leia três números e que imprima o maior
e o menor.
'''
print("")

num1 = float(input("Digite o 1º número: "))
num2 = float(input("Digite o 2º número: "))
num3 = float(input("Digite o 3º número: "))

if (num1 < num2) and (num1< num3):
    menor = num1
if (num2 < num1) and (num2 < num3):
    menor = num2
if (num3 < num1) and (num3 < num2):
    menor = num3
if (num1 > num2) and (num1 > num3):
    maior = num1
if (num2 > num1) and (num2 > num3):
    maior = num2
if (num3 > num1) and (num3 > num2):
    maior = num3
print(f"Entre {num1}, {num2} e {num3} o menor é {menor} e o maior é {maior}.")
