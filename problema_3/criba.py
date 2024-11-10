def criba_eratostenes(n):
    # Crear una lista de booleanos donde asumimos que todos los números son primos
    primos = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        # Si primos[p] es True, entonces es un número primo
        if primos[p] == True:
            # Actualizar todos los múltiplos de p como no primos
            for i in range(p * p, n + 1, p):
                primos[i] = False
        p += 1

    # Recoger todos los números primos
    return [p for p in range(2, n + 1) if primos[p]]

#n = 10
#primos_hasta_n = criba_eratostenes(n)
#print(f"Primos hasta {n}: {primos_hasta_n}")
