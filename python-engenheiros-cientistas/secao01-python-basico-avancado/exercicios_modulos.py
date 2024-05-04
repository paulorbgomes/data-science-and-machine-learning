G_TERRA = 9.8
G_LUA = 1.6

def peso_lua(massa):
    return massa * G_LUA

def peso_terra(massa):
    return massa * G_TERRA

def imc(peso, altura):
    return float(peso / (altura ** 2))
