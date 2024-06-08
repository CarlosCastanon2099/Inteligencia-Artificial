<div align="center">

# 🤖 **Practica 01** ⚙️



# **Desarollo de un Chatbot con ChatterBot**


</div>



<div align="center">

[![](https://i.pinimg.com/originals/71/51/3b/71513b4e0db5610e5fb35e91c84906c3.gif)](https://www.youtube.com/watch?v=lz4YVXt8vjs)

</div>

----

[Chatterbot.webm](https://github.com/CarlosCastanon2099/Inteligencia-Artificial/assets/108638686/abdd82b9-fe78-4f62-877e-fd1e35c014c9)


----


## **Requerimientos**

Para la presente implementacion hemos contemplado el uso de un entorno virtual el cual ya tiene todo lo necesario para poder ejecutar al Chatbot, sin embargo
en caso de tener exactamente una version de 
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
 como por ejemplo la 
 [![Python 3.7.17](https://img.shields.io/badge/python-3.7.17-blue.svg)](https://www.python.org/downloads/release/python-3717/)
 (la cual es la que usamos en el entorno virtual) podemos instalar los requerimientos siguientes (lo cual no recomendamos y sugerimos enormemente usar el entorno virtual):

-----------------

**spaCy**

La documentacion de spaCy se puede consultar [aqui](https://spacy.io/usage).

```C
> pip install -U pip setuptools wheel
```

```C
> pip install -U spacy
```

```C
> python -m spacy download en_core_web_sm
```

**ChatterBot 1.0.8**

La documentacion de ChatterBot se puede consultar [aqui](https://chatterbot.readthedocs.io/en/stable/setup.html).

```C
> pip install ChatterBot
```

Debemos mencionar nuevamente que instalar lo anterior no es necesario debido a el entorno virtal y que las versiones de las dependencias de spaCy pueden llegar a chocar con las dependencias de ChatterBot
debido a la version de python usada o nuevas versiones de spaCy o ChatterBot.

---

## **Uso**

Para correr el programa `chatterbot_SIA.py` el cual realiza la funcion de un ChatBot:
- Correr desde `Practica-01/` lo siguiente:

Primero activamos el entorno virtual

Linux  : 

```Haskell
\Practica-01$ source myenv/bin/activate
```

Una vez ejecutado lo anterior deberiamos ver lo siguiente:

```Haskell
(myenv) batman@brother-eye:~/Inteligencia-Artificial/Practicas/Practica-01$
```

Ya que estamos en el entorno virtual podemos ejecutar:
```Haskell
\Practica-01$ python3 chatterbot_SIA.py
```

Lo cual deberia verse de esta forma en la terminal:
```Haskell
(myenv) batman@brother-eye:~/Inteligencia-Artificial/Practicas/Practica-01$ python3 chatterbot_SIA.py
```

Al ejecutar lo anterior deberiamos ver lo siguiente:
```Haskell
(myenv) batman@brother-eye:~/Inteligencia-Artificial/Practicas/Practica-01$ python3 chatterbot_SIA.py
List Trainer: [####################] 100%
List Trainer: [####################] 100%
List Trainer: [####################] 100%
List Trainer: [####################] 100%
...
List Trainer: [####################] 100%
List Trainer: [####################] 100%
List Trainer: [####################] 100%
List Trainer: [####################] 100%


Este es el Recomendabot
Te puedo recomendar musica, Peliculas, Videojuegos, contarte un chiste, o darte un dato curioso
Si quisiera terminar la interaccion, proceda a despedirse :D
User: |
```



Ejemplo de uso con el programa:

```C#
Este es el Recomendabot
Te puedo recomendar musica, Peliculas, Videojuegos, contarte un chiste, o darte un dato curioso
Si quisiera terminar la interaccion, proceda a despedirse :D
User: Hola
Bot: Hola
User: recomendar musica
Bot: Te recomiendo la cancion "Uprising" de Muse
User: Podrias sugerirme una pelicula
Bot: Te recomiendo la pelicula 300 dirigida por Zack Snyder
User: Cuentame un chiste
Bot: Que le dijo una iguana a su hermana gemela somos iguanitas
User: alguna curiosidad intrigante
Bot: Puedes hacerme sonreir
User: recomienda algun videojuego                                                            
Bot: Te recomiendo el videojuego Halo
User: Adios
Gracias por usar el recomendabot
Tiene alguna sugerencia para mejorar el bot
Tu: No, muchas gracias
Gracias, nos sirve mucho su sugerencia, que tenga un buen dia
```



