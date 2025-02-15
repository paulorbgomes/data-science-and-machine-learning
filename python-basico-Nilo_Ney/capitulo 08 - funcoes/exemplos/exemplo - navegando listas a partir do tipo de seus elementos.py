'''
Imagine uma lista na qual os elementos podem ser do tipo string
ou lista. Se forem do tipo string, imprima-os. Se forem do tipo
lista, imprima cada elemento dessa lista.
'''
print("")

L = ["a", ["b", "c", "d"], "e"]
for i in L:
    if type(i) is str:
        print(i)
    elif type(i) is list:
        for j in i:
            print(j)
