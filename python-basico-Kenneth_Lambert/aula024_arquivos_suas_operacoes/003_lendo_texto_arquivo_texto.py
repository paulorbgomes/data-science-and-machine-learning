# Lendo texto de um arquivo de texto

'''
f = open("myfile.txt", 'r')
text = f.read()
#print(text)
f.close()
'''

'''
f = open("myfile.txt", 'r')
for line in f:
    print(line)
'''

f = open("myfile.txt", 'r')
while True:
    line = f.readline()
    if line == "":
        break
    print(line)
