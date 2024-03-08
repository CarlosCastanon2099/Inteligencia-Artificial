import re


letras = [
    'a', 'e', 'r', 'o', 'i', 'n', 'c', 't', 'l', 's', 'd', 'm', 'u', 'p', 'b', 'g',
    'h', 'f', 'v', 'z', 'j', 'q', 'ñ', 'y', 'x', 'k', 'w'
]

"""
# Version con acentos
letras = [
    'a', 'e', 'r', 'o', 'i', 'n', 'c', 't', 'l', 's', 'd', 'm', 'u', 'p', 'b', 'g',
    'h', 'f', 'v', 'o', 'z', 'i', 'j', 'q', 'a', 'ñ', 'e', 'y', 'x', 'u', 'ü', 'k', 'w', 'î'
]
"""

"""
"\da\dbl\d"
"""

def informada(palabra, letras_usadas):
    patron = obtenerPatron(palabra, ''.join(letras_usadas))
    coincidencia = ""

    with open("Diccionario.txt", 'r', encoding="utf8") as diccionario:
        for linea in diccionario.readlines():
            if re.search(patron, linea):
                coincidencia = linea
                break

    if coincidencia == "":
        for letra in letras:
            if letra not in letras_usadas:
                return letra
    
    print("Palabra en coincidencia: " + coincidencia)
    for letra_comun in letras:
        if letra_comun in coincidencia and letra_comun not in letras_usadas:
            return letra_comun
    return '?'

def obtenerPatron(palabra, letras_usadas):
    letras_excluidas = "[^%s\s]" % letras_usadas
    patron = '^'
    for letra in palabra:
        if letra == '_':
            patron += letras_excluidas
        else:
            patron += letra
    patron += '$'
    print("El patron regex a buscar: " + patron)
    return patron


if __name__ == "__main__":
    print( "Palabra recibida : \"p_blo\" " )
    print("Letras usadas = ['p','b','l','o']")
    print("Letra a buscar: " + informada("p_blo", ['p','b','l','o']))