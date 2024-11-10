# Buscador de Números Primos usando la Criba de Eratóstenes

Este programa implementa la Criba de Eratóstenes para encontrar números primos y permite buscar el n-ésimo número primo en la secuencia.

## Descripción

El programa utiliza el algoritmo de la Criba de Eratóstenes para generar números primos y tiene dos funcionalidades principales:
1. Genera una lista de números primos hasta un límite dado
2. Encuentra el n-ésimo número primo en la secuencia, expandiendo el rango de búsqueda si es necesario

## Algoritmo de la Criba de Eratóstenes

El algoritmo funciona de la siguiente manera:
1. Crea una lista de números del 2 hasta el límite especificado
2. Para cada número no tachado en la lista:
   - Marca como None todos sus múltiplos
   - Cuenta el número como primo
3. Al final, elimina todos los None y devuelve los números restantes (que son primos)

## Requisitos

- Python 3.x

## Uso

Ejecuta el programa desde la línea de comandos proporcionando la posición del número primo que deseas encontrar:

```bash
python nesimo_primo.py <posicion>
```

### Ejemplo
```bash
python nesimo_primo.py 10
```
Esto mostrará el décimo número primo.

## Estructura del Código

- `cribado_erastostenes(n)`: Implementa la Criba de Eratóstenes
  - Parámetros:
    - `n`: Límite superior hasta donde buscar números primos
  - Retorna: 
    - `total`: Cantidad de números primos encontrados
    - `primos`: Lista de números primos encontrados

## Características Especiales

- Búsqueda Dinámica: Si el n-ésimo primo buscado no se encuentra en el rango inicial (hasta 100), el programa automáticamente expande el rango de búsqueda multiplicando por 100 en cada iteración hasta encontrar el número deseado.

## Dependencias

- `sys`: Para procesar argumentos de línea de comandos


## Limitaciones y Consideraciones

- El programa asume que se ingresa un número entero positivo como argumento
- Para números muy grandes, el tiempo de ejecución y el uso de memoria aumentarán
- El método de expansión multiplica por 100 en cada iteración, lo que puede ser ineficiente para ciertos casos

## Ejemplos de Uso

```python
# Encontrar el 5to número primo
python nesimo_primo.py 5
# Salida: 11

# Encontrar el 20vo número primo
python nesimo_primo.py 20
# Salida: 71
```
