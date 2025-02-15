'''
Escreva um programa que leia dois números e que pergunte qual
operação você deseja realizar. Você deve poder calcular soma
(+), subtração (-), multiplicação (*) e divisão (/). Exiba o
resultado da operação solicitada.
'''
print("")

from time import sleep
print(30 * "=")
print(f"{'OPERAÇÕES DISPONÍVEIS':^30}")
print(30 * "=")
print(f"{0:<5} SOMA")
print(f"{1:<5} SUBTRAÇÃO")
print(f"{2:<5} MULTIPLICAÇÃO")
print(f"{3:<5} DIVISÃO")
print(30 * "=")
n1 = int(input("Digite o 1º valor: "))
n2 = int(input("Digite o 2º valor: "))
op = int(input("Escolha a operação desejada: "))
if op == 0:
    soma = n1 + n2
    print(f"{n1} + {n2} = {soma}")
elif op == 1:
    sub = n1 - n2
    print(f"{n1} - {n2} = {sub}")
elif op == 2:
    mul = n1 * n2
    print(f"{n1} * {n2} = {mul}")
elif op == 3:
    div = n1 / n2
    print(f"{n1} / {n2} = {div}")
print("Encerrando o programa ...")
sleep(2)
print("Volte sempre!")
