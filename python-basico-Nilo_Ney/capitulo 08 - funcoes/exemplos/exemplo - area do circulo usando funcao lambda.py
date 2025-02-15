'''
Calcule a área de um círculo a partir do seu raio. Utilize uma
função lambda.
'''
print("")

from math import pi

area = lambda r: pi * r**2
r = float(input("Valor do raio: "))
print(f"A área do círculo de raio {r:.2f} uC é {area(r):.2f} uA.")

