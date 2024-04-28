<div align="center">

# 🤖 **Practica 05** 🧬



# **Algoritmos Genéticos en el Juego de la Vida**


</div>



<div align="center">

[![](https://laughingsquid.com/wp-content/uploads/2018/06/Westworld-Intro-LEGO.gif)](https://www.youtube.com/watch?v=fZbusX0dt9o)

</div>

---

## **Requerimientos**

[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/) en adelante.

Para la presente implementacion se contemplaron las bibliotecas adicionales de numpy, pygame y de ipywidgets, en caso de no tenerlas instaladas, ejecutar:

```C
> pip install pygame
```

```C
> pip install numpy
```

```C
> pip install ipywidgets
```

Es importante recordar tambien que debemos asegurarnos de que tenemos instalado [Jupyter](https://jupyter.org/install).

```C
> pip install jupyterlab
```

```C
> pip install notebook
```

## **Preliminares**
La presente contempla dos implementaciones, la primera es de los Automatas Celulares en el Juego de la Vida de Conway, la segunda es
nuestra version modificada del mismo en el que incluimos algoritmos geneticos la cual consiste de lo siguiente:

En esta version genetica, todas las celulas siguen en todo momento las reglas del juego de la vida original, sin embargo, 
ahora tendremos celulas ${\color{red}rojas}$ y celulas ${\color{lightblue}azules}$, aunque ambas celulas sigan el comportamiento original
de Conway, vamos a tener un ligero cambio con las celulas ${\color{lightblue}azules}$, a estas vamos a darles la posibilidad de ${\color{lightgreen}evolucionar}$
para esto codificamos el cromosoma de un automata celular (${\color{lightblue}azul}$) de tal forma que sus genes serán su color y un gen al que llamaremos $poder$
en el momento que se efectuen las reglas del juego de la vida y las celulas se crucen, sus celulas hijas tendran la posibilidad de mutar y con esto cambiar su color 
a uno mas ${\color{blue}oscuro}$  e adquirir al mismo tiempo su gen de $poder$, todo lo anterior le dara a estas ${\color{blue}celulas \space mutadas \space azules}$ la capacidad 
de ocupar el espacio de una celula ${\color{red}roja}$, en otras palabras, les da la posibilidad de aniquilar a las celulas ${\color{red}rojas}$  siempre y cuando se trate de una 
${\color{blue}celula \space azul \space mutada}$.

## **Uso**

Para correr el programa, se debe abrir el Jupyter Notebook en algun editor (como Jupyter nativo, VS Code, etc.).

[Practica-05](./practica05.ipynb)

<!---
Ejemplo De Uso Notebook
-->

https://github.com/CarlosCastanon2099/Inteligencia-Artificial/assets/108638686/1d733b1b-95ae-4328-aa14-ec61c2d171c9



<!---
Ejemplo Conway Normal
-->

https://github.com/CarlosCastanon2099/Inteligencia-Artificial/assets/108638686/1743a8dd-9bd5-4899-80a8-06ed869dfdd5




<!---
Ejemplo Conway Genetico
-->

https://github.com/CarlosCastanon2099/Inteligencia-Artificial/assets/108638686/5ef4b462-eb72-49cb-9071-9fbd8c6ea70c

