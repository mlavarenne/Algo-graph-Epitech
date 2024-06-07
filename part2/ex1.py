import networkx as nx

def appariement_degre_minimum(graph):
    matching = set()
    nodes_sorted = sorted(graph.nodes, key=lambda x: graph.degree[x])
    while nodes_sorted:
        node = nodes_sorted.pop(0)
        if node not in [n for u, v in matching for n in (u, v)]:
            for neighbor in graph.neighbors(node):
                if neighbor not in [n for u, v in matching for n in (u, v)]:
                    matching.add((node, neighbor))
                    nodes_sorted.remove(neighbor)  # Mettre à jour la liste des nœuds non encore appariés
                    break
    return matching

def appariement_degre_maximum(graph):
    matching = set()
    nodes_sorted = sorted(graph.nodes, key=lambda x: -graph.degree[x])
    while nodes_sorted:
        node = nodes_sorted.pop(0)
        if node not in [n for u, v in matching for n in (u, v)]:
            for neighbor in graph.neighbors(node):
                if neighbor not in [n for u, v in matching for n in (u, v)]:
                    matching.add((node, neighbor))
                    break
    return matching

# Créez un graphe (vous pouvez ajouter des nœuds et des arêtes ici)
G = nx.Graph()
G.add_nodes_from([1, 2, 3])
G.add_edges_from([(1, 2), (2, 3)])

# Appelez la fonction pour trouver l'appariement de degré minimum
matching = appariement_degre_minimum(G)

# Affichez l'appariement
print("Appariement de degré minimum :", matching)

# Créez un graphe (vous pouvez ajouter des nœuds et des arêtes ici)
graph = nx.Graph()
graph.add_edges_from([(1, 2), (2, 3), (3, 4)])

# Appelez la fonction
matching = appariement_degre_maximum(graph)

# Affichez le résultat
print("Appariement de degré maximum :", matching)