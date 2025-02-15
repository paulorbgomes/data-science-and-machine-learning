'''
Escreva um programa que calcule o preço a pagar pelo fornecimento
de energia elétrica. Pergunte a quantidade de KWh consumida e o
tipo de instalação: R para residências, I para indústrias e
C para comércios. Calcule o preço a pagar de acordo com a tabela
a seguir (tabela na página 83 do livro texto).
'''
print("")

print(20 * "=")
print(f"{'COELCE':^20}")
print(20 * "=")
print(f"{'R - Residência':<20}")
print(f"{'I - Indústria':<20}")
print(f"{'C - Comércio':<20}")
print(20 * "=")
op = str(input("Escolha a sua opção: ")).strip().upper()[0]
con = float(input("Quantidade de KWh consumida: "))
if op == "R":
    if con <= 500:
        valor = 0.40 * con
        print(f"Preço a pagar: R$ {valor:.2f}")
    else:
        valor = 0.65 * con
        print(f"Preço a pagar: R$ {valor:.2f}")
elif op == "C":
    if con <= 1000:
        valor = 0.55 * con
        print(f"Preço a pagar: R$ {valor:.2f}")
    else:
        valor = 0.60 * con
        print(f"Preço a pagar: R$ {valor:.2f}")
elif op == "I":
    if con <= 5000:
        valor = 0.55 * con
        print(f"Preço a pagar: R$ {valor:.2f}")
    else:
        valor = 0.60 * con
        print(f"Preço a pagar: R$ {valor:.2f}")
