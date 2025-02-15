'''
Escreva um programa que leia dois números. Imprima o resultado
da multiplicação do primeiro pelo segundo. Utilize apenas
operadores de soma para calcular o resultado.
'''
print("")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = 0
for i in range(1,num2+1):
    soma = soma + num1
print(f"A operação {num1} x {num2} é igual a {soma}.")
