'''
Modifique o programa anterior de forma a ler um número n.
Imprima os n primeiros números primos.
'''
print("")

num = int(input("Digite um número: "))
print(f"Números primos até {num}:")
for i in range(1,num + 1):
    passo = 1
    cont = 0
    while passo <= i:
        if i % passo == 0:
            cont = cont + 1
        passo = passo + 1
    if cont == 2:
        print(i)

    

        
    
    
    
        
    
    
