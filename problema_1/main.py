import re
import pandas as pd
import fitz
import pymupdf

filter=r"^[A-Z\s\d?\?\.\,\-]+[\d\/\d of A-Z\d]*[A-Z\d]*$"
filterOnlyLetter=r"^[A-Z]+$"

def lectura(archivo):
    with pymupdf.open(archivo) as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    text = text.replace('�','')
    text = text.split('\n')
    return text

if __name__ == '__main__':

    archivo="Encrypted.pdf"
    text=lectura(archivo)
    #print(text)
    #print(len(text))

    encrypted= [t for t in text if re.match(filter, t)]
    #print(encrypted)
    decrypted=[]
    for line in encrypted:
            decrypted_phrase = ""
            for letter in line:
                if re.match(filterOnlyLetter, letter):
                    decrypted_char=chr((((ord(letter)-65)-16)%26)+65)
                    decrypted_phrase += decrypted_char
                else:
                # Mantén los espacios y otros caracteres sin cambio
                    decrypted_phrase += letter
            decrypted.append(decrypted_phrase)

        # Imprimir el texto descifrado
    print("Texto descifrado:\n", decrypted)
    print(len(decrypted))
    # lista1 = [elemento for elemento in text if elemento not in encrypted]
    # print(lista1)
    # print(len(lista1))
    # print("Agregando-----------------------------------------------")
    # lista1.append(decrypted)
    # print(lista1)
    # print(len(lista1))