# Formatando strings para saida

for exponent in range(7,11,1):
    print(exponent, 10**exponent)

# Justificando strings
s1 = "%6s" % "four"   # justifica a direita
print(s1)

s2 = "%-6s" % "four"  # justifica a esquerda
print(s2)