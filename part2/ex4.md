L'algorithme commence par trier les nœuds en fonction de leur degré, ce qui prend O(n log n) temps.
Ensuite, il parcourt les nœuds triés et trouve les appariements, ce qui prend O(n + m) temps,
où n est le nombre de nœuds et m est le nombre d'arêtes.
Donc, la complexité totale est O(n log n + n + m), ce qui est polynomial.
