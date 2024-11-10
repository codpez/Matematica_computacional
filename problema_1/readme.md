# Desencriptador de Texto PDF

Un script simple para leer un archivo PDF específico, extraer texto que cumple con ciertos patrones y aplicar un descifrado básico mediante desplazamiento de letras.

## Requisitos

- Python 3.x
- Librerías requeridas:
  - re
  - PyMuPDF (fitz)

## Instalación de dependencias

```bash
pip install pymupdf
```

## Uso

1. Asegúrate de tener un archivo llamado "Encrypted.pdf" en el mismo directorio
2. Ejecuta el script:
```bash
python decrypt.py
```

## Funcionamiento

- Lee un PDF específico
- Filtra líneas que cumplen con un patrón predeterminado
- Aplica un desplazamiento de -16 posiciones a las letras mayúsculas
- Mantiene sin cambios los espacios y caracteres especiales

## Notas
- Este script está diseñado para un caso de uso específico
- Solo funciona con el formato de encriptación esperado
- Requiere que el archivo de entrada se llame "Encrypted.pdf"
