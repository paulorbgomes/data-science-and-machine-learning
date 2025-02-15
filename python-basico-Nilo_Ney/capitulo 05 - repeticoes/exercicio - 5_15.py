'''
Escreva um programa para controlar uma pequena máquina
registradora. Você deve solicitar ao usuário que digite o código
do produto e a quantidade comprada. Utilize a tabela de códigos
a seguir para obter o preço de cada produto.
Seu programa deve exibir o total das compras depois que o
usuário digitar 0. Qualquer outro código deve gerar a mensagem
de erro "Código Inválido"
'''
print("")

from time import sleep
print(30 * "=")
print(f"{'MÁQUINA REGISTRADORA':^30}")
print(30 * "=")
print(f"{'CÓDIGO':<10} {'PREÇO (R$)'}")
print(f"{'1':<10} {'0,50'}")
print(f"{'2':<10} {'1,00'}")
print(f"{'3':<10} {'4,00'}")
print(f"{'5':<10} {'7,00'}")
print(f"{'9':<10} {'8,00'}")
print(30 * "=")
preco = 0
while True:
    cod = str(input("Digite o código do produto [0 para finalizar]: ")).strip()
    while cod not in "012359":
        cod = str(input("Código inválido! Por favor digite um código válido: ")).strip()
    if cod == "0":
        print(30 * "=")
        print("Finalizando sua compra ...")
        sleep(1)
        break
    else:
        quantidade = int(input("Digite a quantidade desejada: "))
        if cod == "1":
            preco = preco + quantidade * 0.50
        elif cod == "2":
            preco = preco + quantidade * 1.00
        elif cod == "3":
            preco = preco + quantidade * 4.00
        elif cod == "5":
            preco = preco + quantidade * 7.00
        elif cod == "9":
            preco = preco + quantidade * 8.00
print(30 * "=")
print(f"Total das compras: R$ {preco:.2f}")
print(30 * "=")
print("Obrigado e volte sempre!")




        
        

