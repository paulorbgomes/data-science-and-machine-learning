'''
Escreva um programa que calcule o tempo de uma viagem de carro.
Pergunte a distância a percorrer e a velocidade média esperada
para a viagem.
'''
print("")

distancia = float(input("Qual distância (em Km) você irá percorrer? "))
v_media = float(input("Com qual velocidade (em Km/h) você irá dirigir? "))
duracao = distancia / v_media
print(f"Sua viagem terá uma duração de {duracao} horas. Boa viagem!")
