# Gravando numeros em um arquivo de texto

import random

f = open("integers.txt", 'w')
for count in range(0, 500, 1):
    number = random.randint(1, 500)
    f.write(str(number) + "\n")
f.close()
