# Lendo numeros de um arquivo

f = open("integers.txt", 'r')
theSum = 0
for line in f:
    #print(line)
    line = line.strip()
    number = int(line)
    theSum += number
print("The sum is: ", theSum)
