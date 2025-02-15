'''
Altere o programa anterior de forma a perguntar também o valor
depositado mensalmente. Esse valor será depositado no início de
cada mês, e você deve considerá-lo para o cálculo de juros do
mês seguinte.
'''
print("")

deposito = float(input("Valor do depósito inicial: R$ "))
d0 = deposito
soma_novo = 0
juros = float(input("Taxa de juros (%): "))
for i in range(1,25):
    if i == 1:
        deposito = deposito + (deposito * juros/100)
    else:
        novo = float(input("Quanto você deseja depositar esse mês? R$ "))
        soma_novo = soma_novo + novo
        deposito = deposito + novo
        deposito = deposito + (deposito * juros/100)
    print(f"Mês {i}: R$ {deposito:.2f}")
total_ganho = deposito - soma_novo - d0
print(f"Em 24 meses você ganhou R$ {total_ganho:.2f} em juros.")
    
