'''
Escreva um programa que pesquise se um elemento está ou não
em uma lista, verificando do primeiro ao último elemento.
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
        
pos = []
cont = 0
print()
resp = int(input("Qual número você que saber se está na lista? "))
for i in range(0,len(lista)):
    if lista[i] == resp:
        cont = cont + 1
        pos.append(i + 1)
print()
if cont == 0:
    print(f"O valor {resp} não foi encontrado na lista.")
else:
    print(f"O valor {resp} foi encontrado na(s) posição(ões) {pos}.")
        
