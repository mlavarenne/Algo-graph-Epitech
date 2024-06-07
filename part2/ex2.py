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

def charger_graphe(fichier):
    graph = nx.Graph()
    with open(fichier, 'r') as f:
        n = int(f.readline().strip())
        for line in f:
            u, v = map(int, line.strip().split())
            graph.add_edge(u, v)
    return graph

graph = charger_graphe('graphe_test.txt')
matching_min = appariement_degre_minimum(graph)
matching_max = appariement_degre_maximum(graph)

def est_valide(matching):
    seen = set()
    for u, v in matching:
        if u in seen or v in seen:
            return False
        seen.add(u)
        seen.add(v)
    return True

print(est_valide(matching_min))  # Doit retourner True
print(est_valide(matching_max))  # Doit retourner True
