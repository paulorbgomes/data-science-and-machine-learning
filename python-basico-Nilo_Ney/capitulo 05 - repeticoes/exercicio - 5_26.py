'''
Escreva um programa que calcule o resto da divisão inteira entre
dois números. Utilize apenas as operações de soma e subtração
para calcular o resultado.
'''
print("")

num0 = int(input("Digite um número inteiro: "))
num = num0
div = int(input("Você deseja dividir esse número por qual valor? "))
sub = num - div
cont = 1
while True:
    if sub > 0 and sub >= div:
        cont = cont + 1
        sub = sub - div
    else:
        break
print(f"A divisão entre {num0} e {div} é igual à {cont} com resto {sub}.")
