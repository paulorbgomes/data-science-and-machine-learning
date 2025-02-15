'''
Escreva um programa para calcular a redução do tempo de vida de
um fumante. Pergunte a quantidade de cigarros fumados por dia e
quantos anos ele já fumou. Considere que um fumante perde 10
minutos de vida a cada cigarro, e calcule quantos dias de vida
um fumante perderá. Exiba o total em dias.
'''
print("")

cigarros = int(input("Quantos cigarros você fuma por dia? "))
anos = int(input("Há quantos anos você fuma? "))
q_cigarros = cigarros * 365 * anos
tminutos = q_cigarros * 10
tdias = tminutos / (24 * 60)
print(f"Você fumou aproximadamente {q_cigarros} cigarros, totalizando {int(tdias)} dias de vida perdidos para o vício.")
