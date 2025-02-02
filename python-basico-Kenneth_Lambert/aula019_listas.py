# Listas

lista = []
lista = ["greater"]
lista = ["greater", "less"]
lista = ["greater", "less", 10]
lista = ["greater", ["less", 10]]
print(lista)

# Metodos em listas
print(dir(lista))

testList = []
testList.append(34)
testList.append(22)
testList.sort()
testList.pop()
testList.insert(1, 34)
testList.insert(1, 55)
testList.pop(1)
testList.remove(22)
print(testList)

print("Python is cool".split())
print("".join(['Python ', 'is ', 'cool']))