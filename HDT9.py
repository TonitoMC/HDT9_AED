import networkx as nx
import csv
import numpy as np
import matplotlib.pyplot as plt
import heapq
destinations_set = set()



#Funcion que lee el archivo, agrega las ciudades a un set (para que se creen los nodos).
#Agrega las rutas a una lista de tuplas

G = nx.Graph()

G.add_nodes_from(["Pueblo Paleta", "Aldea Azalea", "Ciudad Safiro", "Ciudad Lavanda", "Aldea Fuego"])

G.add_edge("Pueblo Paleta", "Aldea Azalea", weight = 100)
G.add_edge("Aldea Azalea","Ciudad Safiro" , weight = 150)
G.add_edge("Pueblo Paleta", "Ciudad Safiro", weight = 800)
G.add_edge("Ciudad Lavanda", "Aldea Fuego", weight = 800)
pos = nx.spring_layout(G, k=0.9, iterations=30)

nx.draw(G, pos, arrows=None, with_labels=True, node_size = 450)

def sort_by_value(dictionary):
    return dict(sorted(dictionary.items(), key=lambda item: item[1]))

#Dijkstra
def Dijkstra(startNode):
    #Crea una lista con los nodos no visitados
    unvisited_nodes = list(G)
    #Crea un diccionario con todos los nodos en infinito, excepto el nodo inicial
    distances = {node: np.inf for node in G.nodes()}
    #Se crea un diccionario vacio para las distancias de cada nodo, esto asegura que unicamente se desplieguen las
    #salidas posibles.
    out_distances = {}
    distances[startNode] = 0
    #Crea un min-heap, unicamente con el primer nodo y el valor 0 inicialmente
    heap = [(0, startNode)]
    heapq.heapify(heap)
    #Se inicia un loop hasta que el heap se encuentre vacio
    while heap:
        #La distancia actual y el nodo actual se setean con los primeros valores del heap (los menores)
        current_distance, current_node = heapq.heappop(heap)
        #Revisa que el nodo se encuentre en los nodos ya visitados
        if current_node not in unvisited_nodes:
            continue
        #Marca el nodo como visitado
        unvisited_nodes.remove(current_node)
        #Recorre cada uno de los vecinos del nodo actual
        for neighbor in G[current_node]:
            #La diatancia hacia el vecino actual es el atributo de la relacion
            distance_to_neighbor = G[current_node][neighbor].get("weight", 1)
            #Si la distancia del nodo de origen hacia el nodo actual + la distancia al vecino es  menor que el valor
            #actual del vecino, se actualizan el diccionario y el heap
            if current_distance + distance_to_neighbor < distances[neighbor]:
                distances[neighbor] = current_distance + distance_to_neighbor
                heapq.heappush(heap, (distances[neighbor], neighbor))
        out_distances[current_node] = current_distance
    print(out_distances)

Dijkstra("Pueblo Paleta")

plt.show()