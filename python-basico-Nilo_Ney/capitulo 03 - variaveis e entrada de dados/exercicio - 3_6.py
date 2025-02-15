'''
Escreva um programa que será utilizado para decidir se um aluno
foi ou não aprovado. Para ser aprovado, todas as médias do
aluno devem ser maiores que 7. Considere que o aluno cursa
apenas três matérias, e que a nota de cada uma está armazenada
nas seguintes variáveis: matéria1, matéria2 e matéria3.
'''
print("")

materia1 = float(input("Nota primeira matéria: "))
materia2 = float(input("Nota na segunda matéria: "))
materia3 = float(input("Nota na terceira matéria: "))
media = (materia1 + materia2 + materia3) / 3
print(f"Com as notas {materia1:.1f}, {materia2:.1f} e {materia3:.1f} sua média é: {media:.1f}.")
if media >= 7:
    print("Você está APROVADO ... Parabéns!")
else:
    print("Você está REPROVADO ... Estude mais!")
