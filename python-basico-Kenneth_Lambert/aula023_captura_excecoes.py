# Captura de excecoes

'''
    Sintaxe:
        try:
            <instrucoes>
        except <tipo de excecao>:
            <instrucoes>
'''

def safeIntegerInput(prompt):
    """
    Solicita ao usuario um numero inteiro e retorna o inteiro se estiver bem formado. 
    Caso contrario, imprime uma mensagem de erro e repete este processo ...
    """
    inputString = input(prompt)
    try:
        number = int(inputString)
        return number
    except ValueError:
        print("Error in number format: ", inputString)
        return safeIntegerInput(prompt)
    

if __name__ == "__main__":
    age = safeIntegerInput("Enter your age: ")
    print("Your age is ", age)
       