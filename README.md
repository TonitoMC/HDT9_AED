# Hoja de Trabajo 9: Grafos y Dijkstra
### Autores: José Antonio Mérida Castejón y Adrián López
Este programa implementa un sistema para agendar viajes, lee datos de un archivo llamado "rutas.txt" que contiene la estación de salida, el destino y el costo.

El archivo "rutas.txt" sigue el siguiente formato:
```
"Pueblo Paleta", "Aldea Azalea", 100
"Aldea Azalea", "Ciudad Safiro", 150
"Pueblo Paleta", "Ciudad Safiro", 800
"Ciudad Lavanda", "Aldea Fuego", 300
```
Al iniciar el programa se despliega un grafo que muestra las rutas del archivo, al igual que el costo entre cada salida y destino. 

![image](https://github.com/TonitoMC/HDT9_AED/assets/138615863/6d3ece7b-7db9-45f5-b4b1-c12d2b207797)

Luego se le pide al usuario ingresar el nombre de la estación de salida, se utiliza el algoritmo de Dijkstra para determinar las rutas más cortas para cada destino posible. En el caso de elegir como estación de salida "Pueblo Paleta" se obtiene el siguiente output:
```
Destino: Aldea Azalea, Ruta: Pueblo Paleta -> Aldea Azalea, Distancia: 100
Destino: Ciudad Safiro, Ruta: Pueblo Paleta -> Aldea Azalea -> Ciudad Safiro, Distancia: 250
```
Adicionalmente se genera el siguiente Grafo:

![image](https://github.com/TonitoMC/HDT9_AED/assets/138615863/b73cce69-8ca4-4462-86c8-b3e3be4ed8d4)

## Instalación
Este proyecto fue escrito en [Python](https://www.python.org/). Utiliza [NetworkX](https://networkx.org/), [Numpy](https://numpy.org/) y [Matplotlib](https://matplotlib.org/), por lo cuál es necesario tener instaladas estas dependencias para asegurar el funcionamiento correcto del programa.
