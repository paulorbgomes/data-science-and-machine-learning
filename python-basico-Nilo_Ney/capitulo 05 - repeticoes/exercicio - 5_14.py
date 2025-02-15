'''
Escreva um programa que leia números inteiros no teclado. O
programa deve ler os números até que o usuário digite 0 (zero).
No final da execução, exiba a quantidade de números digitados,
assim como a soma e a média aritmética.
'''
print("")

qde = 0
soma = 0
while True:
    num = int(input("Digite um número inteiro: "))
    if num != 0:
        qde = qde + 1
        soma = soma + num
    else:
        break
print()
print(f"Você digitou {qde} números válidos.")
print(f"A soma dos números digitados é {soma}")
print(f"A média aritmética dos números digitados é {soma/qde}")
