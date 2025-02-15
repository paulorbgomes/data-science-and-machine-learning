'''
Escreva um programa que pergunte o depósito inicial e a taxa de
juros de uma poupança. Exiba os valores mês a mês para os 24
primeiros meses. Escreva o total ganho com juros no período.
'''
print("")

deposito = float(input("Valor do depósito inicial: R$ "))
d0 = deposito
juros = float(input("Taxa de juros (%): "))
for i in range(1,25):
    deposito = deposito + (deposito * juros/100)
    print(f"Mês {i}: R$ {deposito:.2f}")
total_ganho = deposito - d0
print(f"Em 24 meses você ganhou R$ {total_ganho:.2f} em juros.")
    
