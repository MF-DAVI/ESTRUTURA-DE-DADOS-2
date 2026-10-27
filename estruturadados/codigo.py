import networkx as nx
import matplotlib.pyplot as pyplot
G = nx.Graph()
G.add_edges_from([

   (1,2), (1,3),
   (2,4), (2,5),
   (4,5), (3,6)
])
visitados = set()
ordem = []
pilha = [1]

while pilha:
    v = pilha.pop()

    if v not in visitados:
        visitados.add(v)
        ordem.append(v)
        vizinhos = sorted(G.neighbors(v), reverse=True)
        for u in vizinhos:
            if u  not in visitados:
                pilha.append(u)
pyplot.show()         
print(ordem) #[1,2,3,4,5,6]