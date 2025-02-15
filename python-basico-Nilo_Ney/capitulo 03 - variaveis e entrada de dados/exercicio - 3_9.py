'''
Escreva um programa que leia a quantidade de dias, horas,
minutos e segundos do usuário. Calcule o total em segundos.
'''
print("")

dias = int(input("Dias: "))
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

c_minutos = 60 * minutos
c_horas = 60 * 60 * horas
c_dias = 24 * 60 * 60 * dias
c_total = c_dias + c_horas + c_minutos + segundos

print(f"{dias} dias + {horas} horas + {minutos} minutos + {segundos} segundos totalizam {c_total} segundos")

