'''
Escreva um programa que exiba os resultados da tabuada de um
número. O usuário também deve indicar o início e o fim da
tabuada, em vez de começar com 0 até 10.
'''
print("")

n = int(input("Tabuada de: "))
inicio = int(input("Início da tabuada: "))
fim = int(input("Fim da tabuada: "))
for i in range(inicio,fim + 1):
    print(f"{n} x {i} = {n * i}")
