'''
Escreva um programa que gere um dicionário, em que cada chave
seja um caractere, e seu valor seja o número desse caractere
encontrado em uma frase lida.
Ex: O rato -> {"O":1, "r":1, "a":1, "t":1, "o":1}
'''
print("")

memoria = []
dicionario = {}
frase = str(input("Digite uma frase: ")).strip()
for i in frase:
    if i not in memoria:
        memoria.append(i)

for i in range(0,len(memoria)):
    cont = 0
    for j in frase:
        if (j == memoria[i]):
            cont = cont + 1
        dicionario[memoria[i]] = cont
if " " in dicionario:
    del dicionario[" "]
print(dicionario)

    
