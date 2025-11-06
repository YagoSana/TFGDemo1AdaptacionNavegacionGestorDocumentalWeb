# Demo1 para comprender el uso de networkX
import networkx as nx

# Crear un grafo dirigido
G = nx.DiGraph()

# NetworkX añade nodos automaticamente al crear aristas
# Leer de un documentod de texto de entrada, los nodos del grafo
# Los 2 primeros valores son el num de nodos y aristas
# El resto son las aristas del grafo

nombre_archivo = "entrada.txt"
with open(nombre_archivo, 'r') as f:
    #lee la primera linea que pero no es necesario en NetworkX para construir el grafo
    primera_linea = f.readline()

    for linea in f:
        nueva_linea = linea.strip()

        if nueva_linea: #si la linea tiene contenido
            valores = nueva_linea.split()
            if len(valores) >= 2:
                u = int(valores[0])
                v = int(valores[1])
                G.add_edge(u, v)

print("Nodos del grafo:")
print(G.nodes())
print("Aristas del grafo:")
print(G.edges())

# Aplicar algoritmo PageRank
pagerank = nx.pagerank(G)
print("PageRank de los nodos:")
print(pagerank)

# Ordenar los nodos por su valor de PageRank
sorted_pagerank = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)
print("Nodos ordenados por PageRank:")
for node, rank in sorted_pagerank:
    print(f"Nodo {node}: {rank:.5f}")
