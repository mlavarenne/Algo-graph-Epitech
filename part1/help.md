### Partie 1 : Le Problème du Déneigement

#### 1.1 Introduction

Le problème du déneigement consiste à minimiser le temps d'attente moyen des maisons avant que la neige soit nettoyée devant leur porte. Les maisons sont situées sur une route unidimensionnelle, et le chasse-neige part de la position 0.

#### 1.2 Étapes de Réalisation

##### Exercice 1 : Cas non optimaux avec tri ou approche gloutonne

**Objectif** : Trouver un cas où l'ordre optimal de nettoyage n'est pas obtenu par tri ou par l'approche gloutonne.

1. **Choisir n et configurer les positions** :
   - Choisissez un petit n, par exemple entre 5 et 10.
   - Déterminez les positions des maisons de manière à ce que ni le tri des positions ni l'approche gloutonne ne soient optimaux.
   - Exemple :
     ```python
     positions = [2.0, -3.0, 1.5, -1.0, 4.0]
     ```

2. **Calculer les temps d'attente moyens** :
   - Implémentez les deux méthodes de nettoyage (tri et glouton).
   - Comparez les temps d'attente moyens avec un ordre optimal que vous aurez déterminé manuellement.

3. **Comparer les méthodes** :
   - Calculez et comparez les temps d'attente moyens pour les trois méthodes (tri, glouton, optimal).
   - Exemple :
     ```python
     def tri_positions(positions):
         return sorted(positions)
     
     def glouton(positions):
         current_position = 0
         order = []
         while positions:
             closest = min(positions, key=lambda x: abs(x - current_position))
             order.append(closest)
             positions.remove(closest)
             current_position = closest
         return order
     
     def temps_attente_moyen(positions, ordre):
         temps_total = 0
         current_position = 0
         for pos in ordre:
             temps_total += abs(current_position - pos)
             current_position = pos
         return temps_total / len(positions)
     ```

##### Exercice 2 : Algorithme en Temps Polynomial

**Objectif** : Proposer et implémenter un algorithme en temps polynomial pour minimiser le temps d'attente moyen.

1. **Algorithme de base** :
   - Une approche pourrait être de toujours choisir la maison la plus proche dans la direction de la majorité des maisons restantes.

2. **Implémentation** :
   - Implémentez la fonction `parcours` qui prend une liste de positions et retourne les positions triées dans l'ordre optimal.
   - Exemple :
     ```python
     import numpy as np

     def parcours(positions):
         # Implémentation de l'algorithme
         positions_sorted = sorted(positions)  # Exemple simplifié avec tri
         return positions_sorted
     
     # Test de la fonction avec n = 1000
     positions_test = np.random.normal(0, 1000, 1000).tolist()
     ordre_optimal = parcours(positions_test)
     ```

3. **Validation et Comparaison** :
   - Implémentez une solution gloutonne pour comparaison.
   - Utilisez des tests statistiques pour comparer les temps d'attente moyens de votre algorithme et de la solution gloutonne.

4. **Performance** :
   - Vérifiez que votre solution donne un temps d'attente inférieur à 90% du temps obtenu avec la solution gloutonne.
   - Ajustez votre algorithme si nécessaire pour améliorer les performances.

##### Exercice 3 : Preuve de Temps Polynomial

**Objectif** : Prouver que votre solution est en temps polynomial.

1. **Analyse de Complexité** :
   - Analyser le temps d'exécution de votre algorithme.
   - Démontrer que chaque étape de votre algorithme peut être effectuée en temps polynomial.

2. **Rédaction de la Preuve** :
   - Rédigez une preuve mathématique dans votre rapport, similaire à l'exemple fourni.
   - Exemple de preuve :
     ```markdown
     Considérons l'algorithme `parcours`. Chaque étape consiste à trier une liste de n éléments, ce qui prend O(n log n) temps. 
     Le reste des opérations consiste à parcourir la liste, ce qui est en O(n). 
     Donc, la complexité totale est O(n log n), ce qui est polynomial.
     ```

#### Conclusion

1. **Finaliser l'implémentation** :
   - Assurez-vous que votre fonction `parcours` est correcte et optimisée.
   - Testez-la avec différents jeux de données pour vérifier sa robustesse.

2. **Rédiger le rapport** :
   - Incluez des explications sur votre méthode, des comparaisons de performance, et la preuve de temps polynomial.
   - Fournissez des graphiques et des tableaux pour illustrer vos résultats.

En suivant ces étapes, vous serez en mesure de compléter la partie 1 du projet de manière efficace. Bonne chance !