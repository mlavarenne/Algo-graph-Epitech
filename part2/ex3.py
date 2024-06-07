import time
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

def comparer_heuristiques(graph):
    start = time.time()
    matching_min = appariement_degre_minimum(graph)
    time_min = time.time() - start

    start = time.time()
    matching_max = appariement_degre_maximum(graph)
    time_max = time.time() - start

    return len(matching_min), time_min, len(matching_max), time_max

graph = nx.erdos_renyi_graph(100, 0.1)

taille_min, temps_min, taille_max, temps_max = comparer_heuristiques(graph)
print(f"Heuristique Degré Minimum: Taille = {taille_min}, Temps = {temps_min}s")
print(f"Heuristique Degré Maximum: Taille = {taille_max}, Temps = {temps_max}s")
