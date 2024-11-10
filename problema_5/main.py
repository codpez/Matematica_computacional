from factorizacion import factorizacion_prima
import sys
import math

def lcm(a,b):
    aFp= factorizacion_prima(a)
    bFp= factorizacion_prima(b)
    elmaChico=[]
    conteo_lista1 = {}
    conteo_lista2 = {}
    for num in aFp:
        conteo_lista1[num] = conteo_lista1.get(num, 0) + 1 
    
    for num in bFp:
        conteo_lista2[num] = conteo_lista2.get(num, 0) + 1
    
    # Obtener todos los números únicos de ambas listas
    todos_numeros = set(aFp) | set(bFp)
    
    elmaChico = []
    for num in sorted(todos_numeros):

        max_ocurrencias = max(conteo_lista1.get(num, 0), conteo_lista2.get(num, 0))
        elmaChico.extend([num] * max_ocurrencias)
    
    return elmaChico


if __name__ == '__main__':
    num1 = (int(sys.argv[1]))
    num2 = (int(sys.argv[2]))

    lessCm=lcm(num1,num2)
    print(f'El mínimo común multiplo de {num1} y {num2} es {lessCm} que en total es {math.prod(lessCm)}')