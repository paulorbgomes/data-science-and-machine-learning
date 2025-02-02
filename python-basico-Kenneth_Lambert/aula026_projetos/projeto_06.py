'''
O departamento de folha de pagamento mantem uma lista de informacoes do funcionario para cada periodo
de pagamento em um arquivo de texto.
O formato da linha do arquivo e:
<sobrenome> <salario por hora> <horas trabalhadas> <salario>
Escreva um programa que insira um nome de arquivo do usuario e imprima um relatorio no terminal dos
salarios pagos aos funcionarios no periodo determinado.
O relatorio deve estar em formato tabular com o cabecalho apropriado.
Cada linha deve conter o nome do funcionario, as horas trabalhadas e os salarios pagos naquele periodo.
'''

f = open("relatorio_funcionarios.txt", 'w')
while True:
    print("[1] Cadastrar Dados")
    print("[X] Sair do Sistema")
    opcao  = input("Opcao desejada? ")

    if opcao == "x" or opcao == "X":
        print("Conexao finalizada!")
        break
    elif opcao == "1":
        nome = input("Nome do funcionario: ")
        salarioHora = float(input("Salario por hora: R$ "))
        horasTrabalhadas = int(input("Horas trabalhadas: "))
        salarioFinal = salarioHora * horasTrabalhadas

        linha = "Nome: " + str(nome) + "; Salario (hora): R$ " + str(salarioHora) + "; Horas: " + str(horasTrabalhadas) + "; Salario: R$ " + str(salarioFinal) + "\n" 
        f.write(linha)
    else:
        print("Opcao inválida!")
f.close()








        
