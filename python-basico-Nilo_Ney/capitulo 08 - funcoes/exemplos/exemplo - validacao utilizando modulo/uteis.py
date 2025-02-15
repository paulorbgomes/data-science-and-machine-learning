def valida_inteiro(msg, minimo, maximo):
    while True:
        num = int(input((msg)))
        if num > maximo or num < minimo:
            print("Número fora do intervalo estabelecido!")
        else:
            print("Valor registrado! Volte sempre!")
            break
