import re
import unicodedata
from Busqueda_informada import informada
from Busqueda_no_informada import no_informada
from Busqueda_genetica import genetica
MAXINTENTOS = 6

def iniciar_juego(palabra, algoritmo):
    
    letras_usadas = []
    print("La palabra a adivinar es: \t", palabra)
    print("El algoritmo seleccionado es: ", algoritmo_a_nombre(algoritmo), "\n")

    errores = 0

    print("Que empieze el juego! :D\n")

    palabra_clave = '_' * len(palabra)
    letra = ""

    while True:
        print("Palabra\t: " + " ".join(palabra_clave))
        if algoritmo == '1':
            letra = no_informada(palabra_clave, letras_usadas)
        elif algoritmo == '2':
            letra = informada(palabra_clave, letras_usadas)
        elif algoritmo == '3':
            letra = genetica(palabra_clave, letras_usadas)
        print(letra)

        letras_usadas.append(letra)

        if letra not in palabra:
            errores += 1
            print("\nLetra erronea, por lo tanto quedan {} intentos\n".format(MAXINTENTOS - errores))

            if errores == MAXINTENTOS:
                print("\nFracaso por falta de intentos, La respuesta es: {}\n" .format(palabra))
                break
            
        else:
            print("\nLa letra \'" + letra + "\' es correcta!!\n")
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    palabra_clave = palabra_clave[:i] + letra + palabra_clave[i+1:] 

            if "_" not in palabra_clave:
                    print("Sorependentemente lo ha logrado!!! :D")
                    break

"""
Funcion para verificar si una palabra tiene acentos
<true/>  Si la palabra tiene acentos
<false/> En otro caso
"""   
def tiene_acentos(palabra):
    return any(
        unicodedata.category(caracter) == 'Mn' 
        for caracter in unicodedata.normalize('NFD', palabra)
    )

"""
Funcion para verificar si una palabra tiene caracteres especiales
<true/>  Si la palabra tiene caracteres especiales
<false/> En otro caso
"""  
def tiene_caracteres_especiales(palabra):
    return bool(re.search(r'[^a-zA-Z\s]', palabra))

"""
Funcion para mostrar el menu de inicio
<return> palabra a adivinar
"""  
def mostrar_menu():
    print("\n¡Bienvenido al juego de ahorcado!\n")
    print("Ingrese una palabra menor a 6 letras y sin acentos para que sea adivinada:\n")
    while True:
        palabra = input()
        if len(palabra) > 5:
            try:
                print("\nOops! La palabra ingresada es muy larga, por favor ingrese una palabra menor a 6 letras:")
                continue
            except Exception as e:
                print("Ocurrio un error:", e)
                continue
        elif len(palabra) == 0:
            print("\nOops! La palabra esta vacia, por favor ingrese una palabra con al menos una letra:")
        elif tiene_acentos(palabra):
            try:
                print("\nOops! La palabra ingresada tiene acentos, por favor ingrese una palabra sin acentos:")
                continue
            except Exception as e:
                print("Ocurrio un error:", e)
                continue
        elif tiene_caracteres_especiales(palabra):
            try:
                print("\nOops! La palabra ingresada tiene caracteres especiales o contiene numeros, por favor ingrese una palabra sin caracteres especiales ni numeros:")
                continue
            except Exception as e:
                print("Ocurrio un error:", e)
                continue
        return palabra.lower()

"""
Funcion para mostrar el menu de algoritmos
<return> numero de algoritmo
"""  
def mostrar_algoritmos():            
    print("\n¡Ahora elige la opción del algoritmo que deseas usar para adivinar la palabra!\n")
    print("1. Algoritmo de busqueda no informada")
    print("2. Algoritmo de busqueda informada")
    print("3. Algoritmo genetico")
    while True:
        algoritmo = input()
        if algoritmo in ['1','2','3']:
            print("\n¡Elegiste el %s!\n" % algoritmo_a_nombre(algoritmo))
        else:
            try:
                print("\nOops! Opcion no valida. Por favor, selecciona una opcion valida del menu:")
                continue
            except Exception as e:
                print("Ocurrio un error:", e)
                continue
        return algoritmo
    
"""
Funcion para pedirle al usuario si quieres volver a jugar
"""  
def salir_juego():            
    print("\n¿Quieres seguir jugando?\nElija el numero de una de opciones:\n")
    print("1. Si")
    print("2. No")
    while True:
        opcion = input()
        if opcion == '1':
            break
        if opcion == '2':
            print("\n\nGracias por jugar al ahorcado!!\nVuelva pronto!!")
            break
        else:
            try:
                print("\nOops! Opcion no valida. Por favor, selecciona una opcion valida del menu:")
                continue
            except Exception as e:
                print("Ocurrio un error:", e)
                continue
        break
    return opcion

"""
Funcion para obtener el nombre del algoritmo a partir de su numero
<return> nombre de algoritmo
"""  
def algoritmo_a_nombre(numero_algoritmo):
    if numero_algoritmo == '1':
        return "Algoritmo de busqueda no informada"
    elif numero_algoritmo == '2':
        return "Algoritmo de busqueda informada"
    elif numero_algoritmo == '3':
        return "Algoritmo genetico"
    return "Algoritmo prohibido???????????? Error"
    

"""
Funcion inicial para ejecutar el algoritmo del ahorcado
"""
if __name__ == "__main__":
    salir = 0
    while(salir != '2'):
        palabra = mostrar_menu()
        algoritmo = mostrar_algoritmos()
        iniciar_juego(palabra, algoritmo)
        salir = salir_juego()

"""   
Diccionario de palabras en español tomado de https://github.com/JorgeDuenasLerin/diccionario-espanol-txt
"""
