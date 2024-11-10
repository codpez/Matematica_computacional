# Calculadora de Factorización Prima

Este programa descompone un número en sus factores primos utilizando la Criba de Eratóstenes para generar números primos hasta la raíz cuadrada del número a factorizar.

## Descripción

El programa implementa la factorización prima siguiendo estos pasos:
1. Calcula la raíz cuadrada del número a factorizar
2. Genera una lista de números primos hasta dicha raíz usando la Criba de Eratóstenes
3. Divide el número repetidamente por cada primo hasta que ya no sea divisible
4. Si queda un residuo mayor que 1, este también es un factor primo

## Requisitos

- Python 3.x
- Módulo `criba.py` con la implementación de `criba_eratostenes()` (debe estar en el mismo directorio)

## Instalación

1. Clona o descarga este repositorio
2. Asegúrate de que el archivo `criba.py` esté presente en el directorio

## Uso

Ejecuta el programa desde la línea de comandos proporcionando un número entero como argumento:

```bash
python factorizacion_prima.py <numero>
```

### Ejemplo
```bash
python factorizacion_prima.py 84
```

El programa mostrará:
1. La lista de números primos hasta la raíz cuadrada del número
2. La lista de factores primos del número ingresado

## Estructura del Código

- `factorizacion_prima(primos, numero)`: Función principal que realiza la factorización
  - Parámetros:
    - `primos`: Lista de números primos hasta la raíz cuadrada del número
    - `numero`: Número a factorizar
  - Retorna: Lista con los factores primos del número

## Algoritmo

El proceso de factorización sigue estos pasos:
1. Recibe una lista de números primos y el número a factorizar
2. Por cada número primo:
   - Divide el número repetidamente mientras sea divisible
   - Almacena cada factor primo encontrado
3. Si queda un residuo mayor que 1, lo agrega como último factor primo

## Dependencias

- `criba.py`: Módulo que contiene la implementación de la Criba de Eratóstenes
- `sys`: Para procesar argumentos de línea de comandos
- `math`: Para calcular la raíz cuadrada

## Notas

- El programa asume que el número ingresado es un entero positivo
- La eficiencia del programa depende de la implementación de la Criba de Eratóstenes
- El programa optimiza la búsqueda de factores generando primos solo hasta la raíz cuadrada
- Si se ingresan argumentos inválidos, el programa generará un error
