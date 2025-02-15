'''
Modifique o exercício anterior para pesquisar dois valores.
Em vez de apenas p, leia outro valor v que também será procurado.
Na impressão, indique qual dos dois valores foi achado primeiro.
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
print()
P = int(input("Digite o valor de P: "))
V = int(input("Digite o valor de V: "))
print()
contP = 0
contV = 0
posP = []
posV = []
for i in range(0,len(lista)):
    if lista[i] == P:
        contP = contP +1
        posP.append(i + 1)
    if lista[i] == V:
        contV = contV + 1
        posV.append(i + 1)
if contP == 0 and contV == 0:
    print(f"Os valores {P} e {V} não foram encontrados na lista.")
elif contP != 0 and contV == 0:
    print(f"O valor {P} foi encontrado nas posições {posP}, enquanto o valor {V} não foi encontrado.")
elif contP == 0 and contV != 0:
    print(f"O valor {V} foi encontrado nas posições {posV}, enquanto o valor {P} não foi encontrado.")
else:
    print(f"Os valores {P} e {V} foram encontrados nas posições {posP} e {posV}, respectivamente.")
    i = 0
    while True:
        if lista[i] == P:
            print(f"O valor {P} foi encontrado primeiro.")
            break
        if lista[i] == V:
            print(f"O valor {V} foi encontrado primeiro.")
            break
        i = i + 1
        











