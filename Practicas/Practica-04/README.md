<div align="center">

# 🤖 **Practica 04** 🌠



# **La poderosa $A^\*$ en el Laberinto**


</div>



<div align="center">

[![](https://i.makeagif.com/media/10-15-2019/OiyKEM.gif)](https://www.youtube.com/watch?v=9wV9_je85DE)

</div>

---

## **Requerimientos**

[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-311/)

Para la presente implementacion se contemplaron las bibliotecas adicionales de numpy, matplotlib y de networkx, en caso de no tenerlas instaladas, ejecutar:

```C
> pip install matplotlib
```

```C
> pip install networkx
```

```C
> pip install numpy
```

Es importante recordar tambien que debemos asegurarnos de que tenemos instalado [Jupyter](https://jupyter.org/install).

```C
> pip install jupyterlab
```

```C
> pip install notebook
```


---

## **Uso**

Para correr el programa del agente inteligente que resuelve un laberinto, se debe abrir el Jupyter Notebook en algun editor (como Jupyter nativo, VS Code, etc.).

[Practica-04](./practica04.ipynb)

Una vez dentro del Notebook, podremos modificarlo para que podamos probar laberintos propios o bien probar con los laberintos aleatorios para veer como es que 
un agente inteligente resuelve el laberinto usando la tecnica de $A^\*$.

Nota: Ya que en nuestros modelos de laberinto no consideramos que anteriormente el laberinto fuera ponderado (que tuviera pesos), decidimos establecer todas las conexiones entre vecinos
a una cantidad de peso $1$, es por esto que si bien se aplica $A^\*$, esta implementacion tiene la particularidad de operar en una grafica donde todos los pesos son $1$, ademas de que a diferencia de las
tecnicas previamente usadas como Back-Tracking, BFS o DFS, $A^\*$ demostro por mucho ser mas eficiente que las anteriores para ser usada por el agente para encontrar la salida del laberinto.
