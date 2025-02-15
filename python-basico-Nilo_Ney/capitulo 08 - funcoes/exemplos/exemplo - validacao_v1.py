'''
Escreva um código para ler um valor inteiro, limitado por um valor
de mínimo e máximo. Esse código repete a entrada de dados até
termos um valor válido.
OBS: Crie um script de validação sem utilizar função.
'''
print("")


while True:
    val = int(input("Digite um valor entre 0 e 5: "))
    if 0 <= val <= 5:
        print("Valor válido! Vamos continuar ...")
        break
    else:
        print("Valor inválido!")

