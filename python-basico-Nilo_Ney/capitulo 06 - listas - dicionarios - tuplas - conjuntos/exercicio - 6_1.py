'''
Crie um programa que leia sete notas de um aluno, armazene
em uma lista e calcule a média aritmética dele.
'''
print("")

notas = []
for i in range(1,8):
    nota = float(input(f"Digite a {i}ª nota: "))
    notas.append(nota)
print(f"As notas do aluno são: {notas}")

soma = 0
for i in range(0,len(notas)):
    soma = soma + notas[i]
media = soma / len(notas)
print(f"A média do aluno é: {media:.2f}")
