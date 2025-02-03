'''
Modos para abertura de arquivos em Python
r (read)   - abre para leitura (e o padrao), gera erro se o arquivo nao existir
w (write)  - abre para escrita, cria o arquivo, se nao existir, e apaga seu conteudo, se existir
x (create) - abre exclusivamente para criacao, gera erro se o arquivo existir
a (append) - abre para escrita, adiciona ao final do arquivo, cria o arquivo, se nao existir
     +     - abreto para atualizacao (leitura e escrita)
b (binary) - modo binario (escrita de bytes)
t (text)   - modo texto (e o padrao)
'''

f = open("relatorio_funcionarios.txt", 'a')
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
