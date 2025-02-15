'''
Faça um programa que percorra duas listas e gere uma terceira sem
elementos repetidos.
'''
print("")

lista1 = []
lista2 = []
lista_geral = []

i = 1
while True:
    num = str(input(f"Insira o {i}º elemento da Lista 1 [X para sair]: ")).strip().upper()
    if num == "X":
        break
    else:
        lista1.append(int(num))
        i = i + 1
print(f"Lista 1: {lista1}")
print()
i = 1
while True:
    num = str(input(f"Insira o {i}º elemento da Lista 2 [X para sair]: ")).strip().upper()
    if num == "X":
        break
    else:
        lista2.append(int(num))
        i = i + 1
print(f"Lista 2: {lista2}")
print()
for i in range(0,len(lista1)):
    if lista1[i] not in lista_geral:
        lista_geral.append(lista1[i])
for i in range(0,len(lista2)):
    if lista2[i] not in lista_geral:
        lista_geral.append(lista2[i])
print(f"Lista geral sem repetiçoes: {lista_geral}")
        
