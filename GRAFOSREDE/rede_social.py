import networkx as nx
import matplotlib.pyplot as plt


# ============================================================
# 1. CONSTRUCAO DO GRAFO NAO DIRECIONADO
# ============================================================

G = nx.Graph()

amizades = [
    ("Ana", "Bruno"),
    ("Ana", "Carla"),
    ("Ana", "Diego"),
    ("Bruno", "Carla"),
    ("Bruno", "Eduardo"),
    ("Carla", "Fernanda"),
    ("Carla", "Gabriel"),
    ("Diego", "Eduardo"),
    ("Eduardo", "Fernanda"),
    ("Fernanda", "Helena"),
    ("Gabriel", "Helena"),
]

G.add_edges_from(amizades)


# ============================================================
# 2. VISUALIZACAO DA REDE SOCIAL
# ============================================================

plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G, seed=42)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=2500,
    font_size=10,
    font_weight="bold",
    edge_color="gray",
)

plt.title("Rede Social Ficticia")
plt.show()


# ============================================================
# 3. GRAU DE CADA VERTICE
# ============================================================

print("\nGRAU DE CADA USUARIO")
print("-" * 35)

for usuario, grau in G.degree():
    print(f"{usuario}: {grau} conexoes")


# ============================================================
# 4. USUARIO COM MAIS CONEXOES
# ============================================================

mais_conectado = max(G.degree(), key=lambda item: item[1])

print("\nUSUARIO MAIS CONECTADO")
print("-" * 35)
print(f"{mais_conectado[0]} possui {mais_conectado[1]} conexoes.")


# ============================================================
# 5. CAMINHOS MAIS CURTOS ENTRE ANA E HELENA
# ============================================================

print("\nCAMINHOS MAIS CURTOS ENTRE ANA E HELENA")
print("-" * 35)

caminhos = list(nx.all_shortest_paths(G, source="Ana", target="Helena"))

for caminho in caminhos:
    print(" -> ".join(caminho))

distancia = nx.shortest_path_length(G, source="Ana", target="Helena")
print(f"Distancia minima: {distancia} arestas")


# ============================================================
# 6. REMOVER A AMIZADE CARLA - FERNANDA
# ============================================================

G.remove_edge("Carla", "Fernanda")

print("\nREMOVENDO A AMIZADE CARLA - FERNANDA")
print("-" * 35)

if nx.has_path(G, "Ana", "Helena"):
    novo_caminho = nx.shortest_path(G, source="Ana", target="Helena")
    print("Ainda existe caminho entre Ana e Helena.")
    print("Novo caminho:", " -> ".join(novo_caminho))
else:
    print("Nao existe mais caminho entre Ana e Helena.")


# Visualizacao apos a remocao
plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G, seed=42)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=2500,
    font_size=10,
    font_weight="bold",
    edge_color="gray",
)

plt.title("Rede apos remover Carla - Fernanda")
plt.show()


# ============================================================
# 7. SUGESTOES DE AMIZADE POR AMIGOS EM COMUM
# ============================================================

print("\nSUGESTOES DE AMIZADE")
print("-" * 35)

sugestoes = []
usuarios = list(G.nodes())

for i in range(len(usuarios)):
    for j in range(i + 1, len(usuarios)):
        pessoa1 = usuarios[i]
        pessoa2 = usuarios[j]

        if not G.has_edge(pessoa1, pessoa2):
            amigos1 = set(G.neighbors(pessoa1))
            amigos2 = set(G.neighbors(pessoa2))
            amigos_comuns = amigos1.intersection(amigos2)

            if amigos_comuns:
                sugestoes.append(
                    (
                        pessoa1,
                        pessoa2,
                        len(amigos_comuns),
                        sorted(amigos_comuns),
                    )
                )

sugestoes.sort(key=lambda item: item[2], reverse=True)

for pessoa1, pessoa2, quantidade, comuns in sugestoes:
    print(
        f"{pessoa1} <-> {pessoa2}: "
        f"{quantidade} amigo(s) em comum -> "
        f"{', '.join(comuns)}"
    )
