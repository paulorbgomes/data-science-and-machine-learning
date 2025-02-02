# Saida de arquivo de texto

'''
OBS: todas as saidas de dados ou entradas de
um arquivo de texto devem ser strings!
'''

# Objeto de arquivo (saida)
f = open("myfile.txt", 'w')
f.write("First line.\nSecond line.\n")

'''
O nao fechamento de um arquivo de saida pode
resultar na perda de dados
'''
f.close()

