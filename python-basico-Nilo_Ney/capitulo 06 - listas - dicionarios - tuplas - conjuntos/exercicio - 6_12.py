'''
Escreva um programa que percorra uma lista e verifique o maior e o menor valor.
valor.
'''
print("")

lista = []
i = 1
while True:
    num = str(input(f"Digite o {i}º elemento da lista [X para sair]: ")).strip().upper()
    if num == "X":
        break
    else:
        lista.append(int(num))
        i = i + 1

for i in range(0,len(lista)):
    if i == 0:
        menor = lista[i]
        maior = lista[i]
    else:
        if lista[i] < menor:
            menor = lista[i]
        if lista[i] > maior:
            maior = lista[i]
print()
print(f"O menor e o maior valores da lista são {menor} e {maior}, respectivamente.")
