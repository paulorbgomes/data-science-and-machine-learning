'''
Escreva um programa que receba o raio de uma esfera (um numero de ponto flutuante) como entrada e produza o diametro, a circunferencia, a area da superficie e o volume da esfera.
'''

import math

def dados(raio):
    # Diametro
    d = 2 * raio
    # Circunferencia
    c = 2 * math.pi * math.pow(raio, 2)
    # Area da superficie
    a = 4 * math.pi * math.pow(raio, 2)
    # Volume
    v = (4 / 3) * math.pi * math.pow(raio, 3)

    print("====================")
    print("Dados da esfera ...")
    print("====================")
    print(f"Raio: {raio} u.c.")
    print(f"Diametro: {d} u.c.")
    print(f"Circunferencia: {c} u.c.")
    print(f"Area: {a} u.a.")
    print(f"Volume: {v} u.v.")
    print("====================")

if __name__ == "__main__":
    raio = float(input("Raio da esfera: "))
    dados(raio)
