def olaMundo():
    print("Olá, Mundo!")

def soma10(a):
    return a + 10

def salario(horas):
    return horas * 25

def salarioBonus(horas):
    return salario(horas) + 50

print(salario(8))
print(salarioBonus(8))
