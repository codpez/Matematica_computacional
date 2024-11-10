import sys

def mcd(a,b):
    while b!=0: # mientras b no sea 0 sigue el ciclo.
        a, b = b, a%b # guardo b en a y despues guardo el residuo de a y b en b. En ese orden
    return a # cuando b=0 retorna a.



if __name__ == '__main__':
    a= int(sys.argv[1])
    b= int(sys.argv[2])
    maximoComunDivisor=mcd(a,b)
    print(f"el Máximo Común Divisor de {a} y {b} es {maximoComunDivisor}")