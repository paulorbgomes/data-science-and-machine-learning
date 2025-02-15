'''
Escreva um programa que leia um número e verifique se é ou não
um número primo (possui apenas dois divisores, 1 e ele mesmo).
Para fazer essa verificação, calcule o resto da
divisão do número por 2 e depois por todos os números ímpares
até o número lido. Se o resto de uma dessas divisões for igual
a zero, o número não é primo. Observe que 0 e 1 não são primos
e que 2 é o único número primo que é par.
'''
print("")

num = int(input("Digite um número: "))
passo = 1
cont = 0
while passo <= num:
    if num % passo == 0:
        cont = cont + 1
    passo = passo + 1
if cont == 2:
    print(f"O número {num} é primo.")
else:
    print(f"O número {num} não é primo.")
    

        
    
    
    
        
    
    
