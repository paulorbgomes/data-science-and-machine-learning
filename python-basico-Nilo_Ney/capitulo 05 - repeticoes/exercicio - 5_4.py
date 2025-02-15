'''
Faça um programa que imprima de 1 até o número digitado pelo
usuário, mas, dessa vez, apenas os números ímpares.
'''
print("")

num = int(input("Digite um número inteiro: "))
for i in range(1,num + 1,2):
    print(i)
