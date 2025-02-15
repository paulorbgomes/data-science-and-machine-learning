'''
Escreva um programa que exiba os resultados da tabuada de um
número.
Ex: 2x1 = 2, 2x2 = 4, ...
'''
print("")

n = int(input("Tabuada de: "))
for i in range(0,11):
    print(f"{n} x {i} = {n * i}")
