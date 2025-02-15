'''
Escreva uma função lambda que soma dois valores e retorna a
soma entre eles.
'''
print("")

soma = lambda a, b: a + b

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
print(f"A soma entre {a} e {b} vale {soma(a, b)}.")
