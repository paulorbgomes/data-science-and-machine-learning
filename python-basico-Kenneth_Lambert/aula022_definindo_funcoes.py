# Definicoes de funcoes

def square(n):
    """
    Calcula e retorna o quadrado de um numero ...
    """
    result = n ** 2
    return result

if __name__ == "__main__":
    help(square)

    test = square(10)
    print(test)