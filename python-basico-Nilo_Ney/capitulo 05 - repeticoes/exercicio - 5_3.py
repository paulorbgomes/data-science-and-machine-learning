'''
Faça um programa para escrever a contagem regressiva do
lançamento de um foguete. O programa deve imprimir
10, 9, 8, ..., 1, 0 e FOGO! na tela.
'''
print("")

from time import sleep
for i in range(10,-1,-1):
    print(f"{i}, ", end="")
    sleep(1)
print("FOGO!")
