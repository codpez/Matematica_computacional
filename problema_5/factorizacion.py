from criba import criba_eratostenes
import math

def factorizacion_prima(numero):
    factorizacion_prima = []
    primos = criba_eratostenes(round(math.sqrt(numero)))
    for numeroPrimo in primos:    
        while numero % numeroPrimo == 0:
            numero = numero // numeroPrimo
            factorizacion_prima.append(numeroPrimo)
    
    # Después del bucle, si queda un número mayor que 1, significa que es primo
    if numero > 1:
        factorizacion_prima.append(numero)
    
    return factorizacion_prima
