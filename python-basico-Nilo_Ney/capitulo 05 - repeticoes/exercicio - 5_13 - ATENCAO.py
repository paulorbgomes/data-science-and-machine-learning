'''
Escreva um programa que pergunte o valor inicial de uma dívida
e o juros mensal. Pergunte também o valor mensal que será pago.
Imprima o número de meses para que a dívida seja paga, o total
pago e o total de juros pago.
'''
print("")

divida = float(input("Digite o valor da sua dívida: R$ "))
juros_mensal = float(input("Juros mensal [%]: "))
pagamento_mensal = float(input("Qual valor será pago mensalmente? R$ "))
print()
print("Análise detalhada da sua dívida ...")
print()
mes = 1
total_pago_juros = 0
total_pago_mes = 0
while divida > 0:
    if divida > pagamento_mensal:
        juros = divida * juros_mensal / 100
        divida = divida - pagamento_mensal + juros
        total_pago_juros = total_pago_juros + juros
        total_pago_mes = total_pago_mes + pagamento_mensal
        print(f"No mês {mes} você pagou R$ {pagamento_mensal:.2f} e ficou devendo R$ {divida:.2f}")
        mes = mes + 1
    if divida <= pagamento_mensal:
        pagamento_mensal = divida
        total_pago_mes = total_pago_mes + pagamento_mensal
        divida = divida - pagamento_mensal
        print(f"No mês {mes} você pagou R$ {pagamento_mensal:.2f} e finalizou seu empréstimo.")
print()
print(f"Sua dívida será paga em {mes} meses")
print(f"Você pagará um total de R$ {total_pago_mes + total_pago_juros:.2f}")
print(f"Você pagou um total de juros de R$ {total_pago_juros:.2f}")
    

    
        
    

