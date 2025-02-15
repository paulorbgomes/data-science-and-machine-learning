'''
A lista de temperaturas de Mons, na Bélgica, foi armazenada na
lista T = [-10, -8, 0, 1, 2, 5, -2, -4]. Faça um programa que
imprima a menor e a maior temperatura, assim como a temperatura
média.
'''
print("")

T = [-10, -8, 0, 1, 2, 5, -2, -4]
soma = 0
for i in range(0,len(T)):
    soma = soma + T[i]
    if i == 0:
        menor = T[i]
        maior = T[i]
    else:
        if T[i] < menor:
            menor = T[i]
        if T[i] > maior:
            maior = T[i]
print(f"Temperatura de Mons: {T}")
print(f"Menor temperatura: {menor}")
print(f"Maior temperatura: {maior}")
print(f"Temperatura média: {soma / len(T)}")

