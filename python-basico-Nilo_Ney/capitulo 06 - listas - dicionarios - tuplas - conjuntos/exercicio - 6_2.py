'''
Faça um programa que leia duas listas e que gere uma terceira
com os elementos das duas primeiras.
'''
print("")

lista1 = []
lista2 = []
lista_geral = []

i = 1
while True:
    num = str(input(f"Digite o {i}º elemento da Lista 1 [X para sair]: ")).strip().upper()
    if num == "X":
        break
    else:
        lista1.append(int(num))
        i = i + 1
print()

i = 1
while True:
    num = str(input(f"Digite o {i}º elemento da Lista 2 [X para sair]: ")).strip().upper()
    if num == "X":
        break
    else:
        lista2.append(int(num))
        i = i + 1

for j in range(0,len(lista1)):
    lista_geral.append(lista1[j])

for j in range(0,len(lista2)):
    lista_geral.append(lista2[j])
print()
print(f"As listas digitadas foram:")
print(lista1)
print(lista2)
print(f"A lista geral é {lista_geral}")
