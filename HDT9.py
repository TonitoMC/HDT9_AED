import networkx as nx
import csv
import numpy as np
import matplotlib.pyplot as plt
import heapq

#Crea el grafo basado en el archivo de texto
G = nx.Graph()
with open("rutas.txt", "r") as file:
    #Para cada linea del archivo
    for line in file:
        #Separa los valores por coma
        parts = line.strip().split(",")
        #Obtiene los nombres de los nodos y el valor de la relacion entre ambos
        node1 = parts[0].strip('"')
        node2 = parts[1].strip().strip('"')
        weight = int(parts[2].strip())
        #Agrega los nodos en caso que no existan
        G.add_node(node1)
        G.add_node(node2)
        #Agrega las relaciones entre nodos
        G.add_edge(node1, node2, weight=weight)

# Dibuja el grafo, se utiliza un spring layout para que no haya overlap entre destinos
pos = nx.spring_layout(G, k=0.9, iterations=30)
nx.draw(G, pos, arrows=None, with_labels=True, node_size=800, font_size=6)
labels= nx.get_node_attributes(G, 'weight')
edge_labels = dict([((n1, n2), G[n1][n2]['weight'])
                    for n1, n2 in G.edges])
nx.draw_networkx_edge_labels(G, pos,edge_labels=edge_labels, font_size = 6)

nodeSet = set(G.nodes())

#Dijkstra
def Dijkstra(startNode):
    # Crea una lista con los nodos no visitados
    unvisited_nodes = list(G)
    # Crea un diccionario con todos los nodos en infinito, excepto el nodo inicial
    distances = {node: np.inf for node in G.nodes()}
    # Se crea un diccionario vacio para las distancias de cada nodo, esto asegura que unicamente se desplieguen las
    # salidas posibles.
    out_distances = {}
    # Se crea un diccionario para almacenar el nodo predecesor de cada nodo durante la ejecución del algoritmo de Dijkstra
    predecessors = {}
    distances[startNode] = 0
    # Crea un min-heap, unicamente con el primer nodo y el valor 0 inicialmente
    heap = [(0, startNode)]
    heapq.heapify(heap)

    # Se inicia un loop hasta que el heap se encuentre vacio
    while heap:
        # La distancia actual y el nodo actual se setean con los primeros valores del heap (los menores)
        current_distance, current_node = heapq.heappop(heap)
        # Revisa que el nodo se encuentre en los nodos ya visitados
        if current_node not in unvisited_nodes:
            continue
        # Marca el nodo como visitado
        unvisited_nodes.remove(current_node)
        # Recorre cada uno de los vecinos del nodo actual
        for neighbor in G[current_node]:
            # La distancia hacia el vecino actual es el atributo de la relacion
            distance_to_neighbor = G[current_node][neighbor].get("weight", 1)
            # Si la distancia del nodo de origen hacia el nodo actual + la distancia al vecino es menor que el valor
            # actual del vecino, se actualizan el diccionario y el heap
            if current_distance + distance_to_neighbor < distances[neighbor]:
                distances[neighbor] = current_distance + distance_to_neighbor
                predecessors[neighbor] = current_node  # Actualiza el nodo predecesor para el vecino
                heapq.heappush(heap, (distances[neighbor], neighbor))
        out_distances[current_node] = current_distance
    D = nx.Graph()
    # Imprime destinos y sus rutas, borra startNode de los valores del diccionario
    del out_distances[startNode]
    for destination, distance in out_distances.items():
        route = [destination]
        predecessor = destination
        # Retrocede desde el destino hasta el nodo inicial
        while predecessor != startNode:
            predecessor = predecessors[predecessor]
            route.append(predecessor)
        route.reverse()  # Invierte la ruta para imprimirla desde el nodo inicial hasta el destino
        print(f"Destino: {destination}, Ruta: {' -> '.join(route)}, Distancia: {distance}")
        for i in range (0, len(route) - 1):
            D.add_node(route[i])
        D.add_edge(startNode, destination, weight=distance)
    pos = nx.spring_layout(D, k=0.9, iterations=30)
    nx.draw(D, pos, arrows=None, with_labels=True, node_size=800, font_size=6)
    edge_labels = dict([((n1, n2), D[n1][n2]['weight'])
                        for n1, n2 in D.edges])
    nx.draw_networkx_edge_labels(D, pos, edge_labels=edge_labels, font_size=6)
    plt.show()


plt.show()
mainMenu = True
while(mainMenu):
    print("Bienvenido al programa para agendar viajes, puedes consultar la imagen generada para ver las posibles rutas")
    print("o igresar el numero correspondiente a cualquiera de las opciones a continuacion")
    print("1. Regenerar grafo (En caso que exista un overlap de los nodos o no se vea claramente)")
    mainSelect = input("2. Ver rutas desde mi estacion de salida")
    if mainSelect == "1":
        pos = nx.spring_layout(G, k=0.9, iterations=30)
        nx.draw(G, pos, arrows=None, with_labels=True, node_size=800, font_size=6)
        labels = nx.get_node_attributes(G, 'weight')
        edge_labels = dict([((n1, n2), G[n1][n2]['weight'])
                            for n1, n2 in G.edges])
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=6)
        plt.show()
    elif mainSelect == "2":
        estacionInput = input("Introduce el nombre de la estacion de salida: ")
        while estacionInput not in nodeSet:
            estacionInput = input("Introduce el nombre de la estacion de salida: ")
        Dijkstra(estacionInput)
