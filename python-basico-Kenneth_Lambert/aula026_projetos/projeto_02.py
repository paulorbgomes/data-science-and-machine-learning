'''
O pagamento semanal total de um funcionario e igual ao salario por hora multiplicado pelo numero total
de horas regulares mais qualquer pagamento de horas extras.

O pagamento de horas extras e igual ao total de horas extras multiplicado por 1.5 vez o salario por hora.

Escreva um programa que receba como entradas o salario por hora, o total de horas regulares e o total de horas extras e exiba o pagamento semanal total de um funcionario.
'''

def salarioSemanal(salarioHora, horasRegulares, horasExtras):
    salarioFinal = (salarioHora * horasRegulares) + (horasExtras * 1.5 * salarioHora)
    print(f"Valor do pagamento semanal: R$ {salarioFinal:.2f}")

if __name__ == "__main__":
    salarioHora = float(input("Salario por hora: R$ "))
    horasRegulares = int(input("Horas regulares trabalhadas: "))
    horasExtras = int(input("Horas extras trabalhadas: "))

    salarioSemanal(salarioHora, horasRegulares, horasExtras)