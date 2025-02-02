'''
Um experimento cientifico padrao e deixar cair uma bola a ver ate que altura ela quica.
Depois que o "quicamento" da bola foi determinado, a razao fornece um indice de quicamento.
Por exemplo, se uma bola largada de uma altura de 10 pes quica 6 pes, o indice e 0,6 e a distancia
total percorrida pela bola e 16 pes apos um salto.
Se a bola continuasse quicando, a distancia depois de dois quiques seria 10 pes + 6 pes + 6 pes + 3,6 = 25,6.
Observe que a distancia percorrida por cada salto sucessivo e a distancia ate o chao mais 0,6 dessa distancia conforme a bola volta a subir. 
Escreva um programa que permita ao usuario inserir a altura inicial da bola e o numero de vezes que a bola pode continuar quicando. A saida deve ser a distancia total percorrida pela bola.
'''

alturaInicial = float(input("Altura inicial do lancamento: "))
numQuiques = int(input("Numero de quiques: "))
