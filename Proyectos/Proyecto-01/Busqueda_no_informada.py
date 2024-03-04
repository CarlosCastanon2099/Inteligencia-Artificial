# ya jalo :D

alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def no_informada(palabra, usadas):
    for letra in alfabeto:
        if letra not in usadas:
            return letra
        
    return None



if __name__ == "__main__":
    palabra_jugada = "abc"
    no_informada(palabra_jugada, ['a','b','c'])