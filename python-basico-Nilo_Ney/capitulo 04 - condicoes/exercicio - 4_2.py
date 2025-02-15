'''
Escreva um programa que pergunte a velocidade do carro de um
usuário. Caso ultrapasse 80 Km/h, exiba uma mensagem dizendo
que o usuário foi multado. Nesse caso, exiba o valor da multa,
cobrando R$ 5 por Km acima de 80 Km/h.
'''
print("")

velocidade = float(input("Qual a sua velocidade [Km/h]? "))
if velocidade <= 80:
    print("Velocidade dentro do permitido. Boa viagem!")
else:
    ex = velocidade - 80
    multa = ex * 5
    print(f"Velocidade acima do permitido! Valor da multa R$ {multa:.2f}.")
    print("Reduza sua velocidade imediatamente!")
