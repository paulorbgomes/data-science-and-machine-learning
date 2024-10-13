# Instrução import

# Importação do modulo completo:
#   import nomeModulo
#   nomeModulo.nomeFuncao()

import math
n = float(input("Digite um valor numérico positivo: "))
raiz = math.sqrt(n)
potencia = math.pow(n, 2)

print("A raiz quadrada de", n, "e:", raiz)
print("O valor de", n, "ao quadrado e:", potencia)


# Importacao de uma funcao especifica de um modulo:
#   from nomeModulo import nomeFuncao
#   nomeFuncao()

from math import pi, pow
raio = float(input("Raio da circunferencia: "))
area = 2 * pi * pow(raio, 2)
print("Area da circ. de raio", raio, ":", area)