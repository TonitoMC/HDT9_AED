import networkx as nx
import csv
import matplotlib.pyplot as plt
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

def get_routes_from_start(startNode):
    return 1

plt.show()