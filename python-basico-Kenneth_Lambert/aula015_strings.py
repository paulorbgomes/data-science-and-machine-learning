# Strings e suas operacoes
# Strings sao imutaveis!

s1 = "String 1"
s2 = "String 2"
print(type(s1), type(s2))

# Operacao +
s3 = s1 + " " + s2
print(s3)

# Indexacao
s = "greater"
print(s[0])

# Operador de fatia
print(s[:])
print(s[2:])
print(s[0])
print(s[2:5])

# Exemplos
n = "Paulo Ricardo Barboza Gomes"
print("Paulo ->", n[0:5])
print("Ricardo ->", n[6:13])
print("Barboza ->", n[14:21])
print("Gomes ->", n[22:])