import sys

def cribado_erastostenes(n):
    
    total=0
    # Creamos una lista con todos los numeros de 2 a n
    numeros = list(range(2,n+1))
    # Iniciamos el cribado 
    for i in numeros:
        if i is None:
            continue
        
        total+=1
        for j in range(i*2,n+1,i):
            numeros[j-2]=None
    return total,[num for num in numeros if num is not None]

total,primos = cribado_erastostenes(100)
busca=int(sys.argv[1])
cont=2
while(True):
    if(busca<total):
        print(primos[busca-1])
        break
    else:
        total,primos = cribado_erastostenes(100*cont)
    cont+=1

#print(f"Total de números encontrados {total}, números primos {primos}")