def soma (a,b):
    return a + b

def subtracao(a,b):
    return a - b

def multiplicacao (a,b):
    return a * b

def potencia (base,expoente):
    return base ** expoente

def raiz_quadrada(x):
    if x < 0 :
        raise ValueError ("Numero negativo")
    return x ** 0.5