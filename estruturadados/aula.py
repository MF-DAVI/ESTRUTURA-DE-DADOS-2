import networkx as nx
import matplotlib.pyplot as pyplot

G = nx.Graph()

G.add_edges_from([

    (1,2),
    (1,3),
    (2,4),
    (2,5),
    (3,5),
    (3,6),
    (4,5)
])

ordem_dfs = list(nx.dfs_preorder_nodes(G, source=1))
print(ordem_dfs)

pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True,
        node_size=1800, font_size=12)
pyplot.show()