'''
Escreva um programa que pergunte a distância que um passageiro
deseja percorrer em Km. Calcule o preço da passagem, cobrando
R$ 0,50 por Km para viagens de até 200 Km, e R$ 0,45 para viagens
mais longas.
'''
print("")

distancia = float(input("Qual distância [em Km] você irá percorrer? "))
if distancia <= 200:
    preco = distancia * 0.50
    print(f"Preço da passagem: R$ {preco:.2f}")
else:
    preco = distancia * 0.45
    print(f"Preço da passagem: R$ {preco:.2f}")
