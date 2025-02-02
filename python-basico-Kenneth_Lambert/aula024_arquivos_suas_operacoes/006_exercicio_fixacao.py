import random

f = open("exercicio_escrita_leitura_processamento.txt", 'w')
for i in range(0, 250, 1):
    number = random.randint(0, 10)
    f.write(str(number) + "\n")
f.close()

'''
f = open("exercicio_escrita_leitura_processamento.txt", 'r')
for i in f:
    print(i)
'''

f = open("exercicio_escrita_leitura_processamento.txt", 'r')
count = 0
add = 0
for i in f:
    n = int(i.strip())
    add = add + n
    count = count + 1
print(f"Soma: {add}, Quantidade: {count}")
    


