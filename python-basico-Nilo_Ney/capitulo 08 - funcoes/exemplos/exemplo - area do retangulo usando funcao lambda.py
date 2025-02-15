'''
Escreva uma função lambda que calcule a área de um retângulo
dados os seus lados.
'''
print("")

area = lambda a, b: a * b

a = float(input("Digite o comprimento do retângulo: "))
b = float(input("Digite a largura do retângulo: "))
print(f"A área do retângulo de lados {a:.2f}x{b:.2f} é {area(a, b):.2f}.")
