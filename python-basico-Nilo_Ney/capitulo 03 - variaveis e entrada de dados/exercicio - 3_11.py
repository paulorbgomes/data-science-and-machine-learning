'''
Faça um programa que solicite o preço de uma mercadoria e o
percentual de desconto. Exiba o valor do desconto e do preço a
a pagar.
'''
print("")

valor = float(input("Valor do produto: R$ "))
percentual = float(input("Percentual de desconto: "))
desconto = valor * percentual / 100
print(f"Seu desconto será de R$ {desconto:.2f}")
pagar = valor -  desconto
print(f"Você pagará R$ {pagar:.2f} pelo produto")
