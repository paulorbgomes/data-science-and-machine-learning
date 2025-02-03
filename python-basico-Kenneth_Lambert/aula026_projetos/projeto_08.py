'''
Escreva um programa que permita ao usuario navegar pelas linhas de texto em um arquivo.

O programa deve solicitar ao usuario um nome de arquivo e inserir as linhas de texto em
uma lista.

O programa entao deve entrar em um laco no qual imprima o numero de linhas no arquivo e
solicite ao usuario um numero de linha.

Os numeros reais das linhas variam de 1 ao numero de linhas no arquivo.

Se a entrada for 0, o programa deve ser encerrado.

Do contrario, o programa deve imprimir a linha associada a esse numero.
'''

nomeArquivo = input("Nome do arquivo para navegacao (.txt): ")
f = open(nomeArquivo, 'w')
linha = 0
while True:
    opcao = input("Cadastrar texto [s ou n]? ")
    if opcao in ["n", "N"]:
        print("Cadastro encerrado. Obrigado!")
        break
    elif opcao in ["s", "S"]:
        linha += 1
        texto = input(f"Texto da {linha}º linha: ")
        f.write(texto + "\n")
    else:
        print("Opção inválida! Tente novamente ...")
f.close()

lista = []
f = open(nomeArquivo, 'r')
for linha in f:
    #print(linha)
    lista.append(linha.strip())
#print(lista)
f.close()

print(f"Número de linhas do arquivo: {len(lista)}")
nLinha = int(input("Escolha o número da linha que desejar analisar: "))
if nLinha == 0:
    print("Programa encerrado ...")
else:
    print(f"Conteúdo associado a linha {nLinha}: ")
    print(lista[nLinha - 1])






        
