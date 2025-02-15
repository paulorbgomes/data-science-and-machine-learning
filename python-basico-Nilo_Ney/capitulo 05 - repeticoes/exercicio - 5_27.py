'''
Escreva um programa que verifique se um número é palíndromo.
Um número é palíndromo se continua o mesmo caso seus dígitos
sejam invertidos.
Exemplos: 454, 10501
'''
print("")

num = str(input("Digite um número inteiro: ")).strip()
cont = 0
for i in range(0,len(num)):
    if num[i] == num[-i-1]:
        cont = cont + 1
if cont == len(num):
    print(f"{num} é palíndromo!")
else:
    print(f"{num} não é palíndromo!")
