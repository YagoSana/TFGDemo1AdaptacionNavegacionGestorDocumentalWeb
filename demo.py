# Demo1 para comprender el uso de networkX
import networkx as nx

# Crear un grafo dirigido
G = nx.DiGraph()

# NetworkX añade nodos automaticamente al crear aristas
G.add_edges_from([(1, 2), (1, 3), (1,4), (1,7), (2, 5), (3, 5), (4, 5), (5, 6), (6, 7), (7, 8), (8, 6)])

print("Nodos del grafo:")
print(G.nodes())
print("Aristas del grafo:")
print(G.edges())

# Aplicar algoritmo PageRank
pagerank = nx.pagerank(G)
print("PageRank de los nodos:")
print(pagerank)

# ORdenar los nodos por su valor de PageRank
sorted_pagerank = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)
print("Nodos ordenados por PageRank:")
for node, rank in sorted_pagerank:
    print(f"Nodo {node}: {rank:.4f}")
