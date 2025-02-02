# Criando classes
# Todos os tipos de dados em Python sao classes ...

class Counter(object):
    """Modela um contador"""

    # Variavel de classe
    instances = 0

    # Construtor
    def __init__(self):
        """Configura o contador"""
        Counter.instances += 1
        self.reset()

    # Metodos mutadores
    def reset(self):
        """Configura o contador com 0"""
        self.value = 0

    def increment(self, amount = 1):
        """Adiciona uma quantia ao contador"""
        self.value += amount

    def decrement(self, amount = 1):
        """Subtrai o valor do contador"""
        self.value -= amount

    # Metodos acessores
    def getValue(self):
        """Retorna o valor do contador"""
        return self.value
    
    def __str__(self):
        """Retorna a representacao de string do contador"""
        return str(self.value)
    
    def __eq__(self, other):
        """Retorna True se self for igual a other ou False, caso contrario"""
        if self is other: return True
        if type(self) != type(other): return False
        return self.value == other.value
    
if __name__ == "__main__":
    c1 = Counter()
    print(c1)
    print(c1.getValue())
    c1.increment()
    print(c1.getValue())
    c1.increment(5)
    print(c1.getValue())
    c1.reset()
    print(c1.getValue())

    c2 = Counter()
    print(Counter.instances)

    print(c1 == c1)
    print(c1 == 0)

    print(c1 == c2)
    print(c1.getValue())
    print(c2.getValue())

    c2.increment()
    print(c1 == c2)
    print(c1.getValue())
    print(c2.getValue())