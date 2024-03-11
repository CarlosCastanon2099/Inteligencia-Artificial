import random

alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def no_informada(palabra, usadas):
    while True:
        letra = random.choice(alfabeto)
        if letra not in usadas and letra not in palabra:
            return letra
    return '?'


'''
if __name__ == "__main__":
    palabra_jugada = "dona"
    print(palabra_jugada)
    print(no_informada(palabra_jugada, ['e','b','c']))
'''
