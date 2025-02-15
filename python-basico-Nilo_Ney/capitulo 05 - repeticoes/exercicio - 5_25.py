'''
Escreva um programa que calcule a raiz quadrada de um número.
Utilize o método de Newton para obter um resultado aproximado.
Sendo N o número a obter a raiz quadrada, considere a base b = 2.
Calcule p usando a fórmula p = (b+(n/b))/2. Agora calcule o
quadrado de p. A cada passo, faça b = p e recalcule p usando a
fórmula apresentada. Pare quando a diferença absoluta entre N e o
quadrado de p for menor que 0.00001.
'''
print("")

print(30 * "-")
print(f"{'MÉTODO DE NEWTON':^30}")
print(30 * "-")
N = float(input("Deseja obter a raiz quadrada de qual número? "))

b = 2
while True:
    p = (b + (N / b)) / 2
    resultado = p ** 2
    b = p
    if abs(N - resultado) < 0.00001:
        break
print(f"A raiz quadrada de {N} é aproximadamente {p:5f}.")
