import numpy as np

def parcours(positions):
    # Implémentation de l'algorithme
    positions_sorted = sorted(positions)  # Exemple simplifié avec tri
    return positions_sorted

# Test de la fonction avec n = 1000
positions_test = np.random.normal(0, 1000, 1000).tolist()
ordre_optimal = parcours(positions_test)
print(ordre_optimal)