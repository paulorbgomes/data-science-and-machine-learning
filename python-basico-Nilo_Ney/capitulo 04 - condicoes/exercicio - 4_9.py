'''
Escreva um programa para aprovar o empréstimo bancário para compra
de uma casa. O programa deve perguntar o valor da casa a comprar,
o salário e a quantidade de anos a pagar. O valor da prestação mensal
não pode ser superior a 30% do salário. Calcule o valor da prestacao
como sendo o valor da casa a comprar dividido pelo número de meses
a pagar.
'''
print("")

valor = float(input("Digite o valor da casa que você deseja comprar: R$ "))
salario = float(input("Salário do comprador: R$ "))
anos = int(input("Em quantos anos deseja pagar? "))
prestacao_max = salario * 30 / 100
meses = anos * 12
prestacao = valor / meses
if prestacao <= prestacao_max:
    print(f"Empréstimo APROVADO!")
    print(f"Você irá pagar {meses} meses de R$ {prestacao:.2f}.")
else:
    print("Empréstimo não autorizado.")
