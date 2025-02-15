'''
Crie uma função lambda que receba dois valores e retorne a média
aritmética entre eles.
'''
print("")

media = lambda a, b: (a + b) / 2

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
print(f"A média aritmética entre {a} e {b} vale {media(a, b)}.")
