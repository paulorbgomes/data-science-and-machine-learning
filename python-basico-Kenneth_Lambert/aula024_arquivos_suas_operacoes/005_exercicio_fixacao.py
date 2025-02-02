# Exercicio de fixacao

# 1. Escrita de arquivo
f = open("exercicio_escrita.txt", 'w')
text = "Linha 1\nLinha 2\nLinha 3\nLinha 4\nLinha 5"
f.write(text)
f.close()

f = open("exercicio_escrita.txt", 'r')
for line in f:
    print(line)
f.close()
