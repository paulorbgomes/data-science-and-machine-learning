'''
Escreva um programa que pergunte a quantidade de Km percorridos
por um carro alugado pelo usuário, assim como a quantidade de
dias pelos quais o carro foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$ 60 por dia e R$ 0,15 por Km rodado.
'''
print("")

distancia = float(input("Qual a quantidade Km percorridos? "))
dias = int(input("Por quantos dias você utilizou o carro? "))
valor_pagar = (60 * dias) + (0.15 * distancia)
print(f"Você deverá pagar R$ {valor_pagar:.2f} pelo aluguel.")
