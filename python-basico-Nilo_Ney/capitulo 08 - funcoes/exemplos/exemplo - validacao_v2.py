'''
Escreva um código para ler um valor inteiro, limitado por um
valor mínimo e máximo. Esse trecho repete a entrada de dados até
termos um valor válido. Esse procedimento deve ser encapsulado
em uma função.
'''
print("")

def verificacao(minimo, maximo):
    while True:
        valor = int(input(f"Digite um valor entre {minimo} e {maximo}: "))
        if minimo <= valor <= maximo:
            print("Valor válido! Vamos continuar ...")
            break
        else:
            print("Valor inválido!")
    return valor

print(verificacao(50, 100))
    
