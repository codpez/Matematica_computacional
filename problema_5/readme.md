# Calculadora de Mínimo Común Múltiplo (LCM)

Este programa calcula el mínimo común múltiplo (LCM) de dos números enteros utilizando la descomposición en factores primos.

## Descripción

El programa implementa el cálculo del mínimo común múltiplo utilizando el siguiente proceso:
1. Descompone ambos números en sus factores primos
2. Cuenta la frecuencia de cada factor primo en ambos números
3. Selecciona la mayor frecuencia de cada factor primo
4. Multiplica todos los factores para obtener el resultado final

## Requisitos

- Python 3.x
- Módulo `factorizacion.py` (debe estar en el mismo directorio)

## Instalación

1. Clona o descarga este repositorio
2. Asegúrate de que el archivo `factorizacion.py` esté presente en el directorio

## Uso

Ejecuta el programa desde la línea de comandos proporcionando dos números enteros como argumentos:

```bash
python main.py <numero1> <numero2>
```

### Ejemplo
```bash
python main.py 12 18
```

El programa mostrará:
- Los números ingresados
- Los factores primos del LCM
- El resultado final del LCM

## Estructura del Código

- `lcm(a,b)`: Función principal que calcula el LCM
  - Parámetros:
    - `a`: Primer número entero
    - `b`: Segundo número entero
  - Retorna: Lista de factores primos del LCM

## Dependencias

El programa depende de:
- `factorizacion.py`: Módulo que contiene la función `factorizacion_prima()`
- `sys`: Para procesar argumentos de línea de comandos
- `math`: Para la función `prod()` que multiplica los elementos de una lista

## Notas

- El programa asume que los números ingresados son enteros positivos
- Si se ingresan argumentos inválidos, el programa generará un error
