'''
Escreva um programa que leia dois números. Imprima a divisão
inteira do primeiro pelo segundo. Utilize apenas os operadores de soma e subtração para calcular o
resultado. Lembre-se de que podemos entender o quociente da
divisão de dois números como a quantidade de vezes que podemos
retirar o divisor do dividendo. Logo, 20/4 = 5, uma vez que
podemos subtrair 4 cinco vezes de 20.
'''
print("")

num1o = int(input("Digite o primeiro número: "))
num2o = int(input("Digite o segundo número: "))
num1 = num1o
num2 = num2o
cont = 0
while True:
    div = num1 - num2
    num1 = div
    cont = cont + 1
    if div == 0:
        print(f"A divisão inteira entre {num1o} e {num2o} é {cont} e resto {div}.")
        break
    elif div < num2:
        print(f"A divisão entre {num1o} e {num2o} é {cont} com resto {div}.")
        break



    
