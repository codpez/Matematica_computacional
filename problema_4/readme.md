# Calculadora de Máximo Común Divisor (MCD)

Este programa implementa el algoritmo de Euclides para calcular el Máximo Común Divisor (MCD) de dos números enteros.

## Descripción

El programa utiliza el algoritmo de Euclides, que se basa en la siguiente propiedad:
- El MCD de dos números `a` y `b` es igual al MCD de `b` y el residuo de `a` dividido por `b`
- Este proceso se repite hasta que el residuo sea 0

## Requisitos

- Python 3.x

## Uso

Ejecuta el programa desde la línea de comandos proporcionando dos números enteros como argumentos:

```bash
python mcd.py <numero1> <numero2>
```

### Ejemplo
```bash
python mcd.py 48 36
```

La salida mostrará:
```
el Máximo Común Divisor de 48 y 36 es 12
```

## Estructura del Código

- `mcd(a,b)`: Implementa el algoritmo de Euclides
  - Parámetros:
    - `a`: Primer número entero
    - `b`: Segundo número entero
  - Retorna: El MCD de los números ingresados

## Algoritmo de Euclides

El algoritmo funciona de la siguiente manera:
1. Se toman dos números `a` y `b`
2. Se divide `a` entre `b` y se obtiene el residuo
3. Si el residuo es 0, `b` es el MCD
4. Si no, se repite el proceso usando `b` como nuevo `a` y el residuo como nuevo `b`

## Dependencias

- `sys`: Para procesar argumentos de línea de comandos

## Notas

- El programa trabaja con números enteros positivos
- Si se ingresan argumentos inválidos, el programa generará un error
- El algoritmo siempre termina después de un número finito de pasos
