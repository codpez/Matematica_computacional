from criba import criba_eratostenes
import sys
import math

def factorizacion_prima(primos, numero):
    factorizacion_prima = []
    
    for numeroPrimo in primos:    
        while numero % numeroPrimo == 0:
            numero = numero // numeroPrimo
            factorizacion_prima.append(numeroPrimo)
    
    # Después del bucle, si queda un número mayor que 1, significa que es primo
    if numero > 1:
        factorizacion_prima.append(numero)
    
    return factorizacion_prima



if __name__ == '__main__':
    numero = int(sys.argv[1])

    raiz_numero = math.sqrt(numero)

    listaDePrimos = criba_eratostenes(round(raiz_numero))
    print(listaDePrimos)
    factores = factorizacion_prima(listaDePrimos,numero)    
    print(factores)
