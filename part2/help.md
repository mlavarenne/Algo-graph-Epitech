### Partie 2 : Choix de Binômes dans une Entreprise (Appariement)

#### 2.1 Introduction

Le but de cette partie est de former des binômes parmi les employés d'une entreprise. Les employés sont représentés par les nœuds d'un graphe \( G \) et les arêtes représentent les paires possibles. Vous devez implémenter des heuristiques pour trouver un appariement maximum.

#### 2.2 Étapes de Réalisation

##### Exercice 1 : Implémentation de deux heuristiques basées sur le degré

**Objectif** : Implémenter deux heuristiques pour trouver un appariement dans un graphe.

1. **Heuristique 1 - Degré Minimum** :
   - **Description** : Sélectionner les sommets de degré minimum en premier pour former des appariements.
   - **Implémentation** :
     ```python
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
                         break
         return matching
     ```

2. **Heuristique 2 - Degré Maximum** :
   - **Description** : Sélectionner les sommets de degré maximum en premier pour former des appariements.
   - **Implémentation** :
     ```python
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
     ```

##### Exercice 2 : Vérification des Heuristiques

**Objectif** : Vérifier que les heuristiques implémentées retournent des appariements valides.

1. **Créer un fichier de test** :
   - Créez un fichier de graphe avec les sommets et les arêtes.
   - Exemple de fichier :
     ```
     5
     0 1
     0 2
     1 2
     1 3
     2 4
     ```

2. **Validation** :
   - Chargez le graphe et appliquez les heuristiques.
   - Vérifiez que les appariements sont valides (aucun nœud n'apparaît dans plus d'une paire).
   - Exemple :
     ```python
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
     ```

##### Exercice 3 : Comparaison des Heuristiques

**Objectif** : Comparer les heuristiques en termes de taille des appariements retournés et de temps de calcul.

1. **Générer des graphes aléatoires** :
   - Utilisez le modèle Erdös-Renyi pour générer des graphes de différents tailles et densités.
   - Exemple :
     ```python
     graph = nx.erdos_renyi_graph(100, 0.1)
     ```

2. **Comparer les appariements** :
   - Appliquez les deux heuristiques et mesurez la taille des appariements et le temps de calcul.
   - Exemple :
     ```python
     import time

     def comparer_heuristiques(graph):
         start = time.time()
         matching_min = appariement_degre_minimum(graph)
         time_min = time.time() - start

         start = time.time()
         matching_max = appariement_degre_maximum(graph)
         time_max = time.time() - start

         return len(matching_min), time_min, len(matching_max), time_max

     taille_min, temps_min, taille_max, temps_max = comparer_heuristiques(graph)
     print(f"Heuristique Degré Minimum: Taille = {taille_min}, Temps = {temps_min}s")
     print(f"Heuristique Degré Maximum: Taille = {taille_max}, Temps = {temps_max}s")
     ```

##### Exercice 4 : Preuve de Temps Polynomial

**Objectif** : Prouver que vos heuristiques sont en temps polynomial.

1. **Analyse de Complexité** :
   - Démontrer que chaque étape des heuristiques est en temps polynomial.
   - Exemple pour l'heuristique de degré minimum :
     ```markdown
     L'algorithme commence par trier les nœuds en fonction de leur degré, ce qui prend O(n log n) temps.
     Ensuite, il parcourt les nœuds triés et trouve les appariements, ce qui prend O(n + m) temps,
     où n est le nombre de nœuds et m est le nombre d'arêtes.
     Donc, la complexité totale est O(n log n + n + m), ce qui est polynomial.
     ```

2. **Rédiger la preuve** :
   - Documentez les preuves de temps polynomial pour les deux heuristiques dans votre rapport.

#### Conclusion

1. **Finaliser l'implémentation** :
   - Assurez-vous que vos fonctions `appariement_degre_minimum` et `appariement_degre_maximum` sont correctes et optimisées.
   - Testez-les avec différents jeux de données pour vérifier leur robustesse.

2. **Rédiger le rapport** :
   - Incluez des explications sur vos méthodes, des comparaisons de performance, et la preuve de temps polynomial.
   - Fournissez des graphiques et des tableaux pour illustrer vos résultats.

En suivant ces étapes, vous serez en mesure de compléter la partie 2 du projet de manière efficace. Bonne chance !