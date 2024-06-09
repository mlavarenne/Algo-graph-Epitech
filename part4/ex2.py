import networkx as nx
import matplotlib.pyplot as plt

# Function to check for Hamiltonian path using backtracking
def is_hamiltonian_path(G):
    def backtrack(v, visited):
        if len(visited) == len(G):
            return True
        for neighbor in G.neighbors(v):
            if neighbor not in visited:
                visited.add(neighbor)
                if backtrack(neighbor, visited):
                    return True
                visited.remove(neighbor)
        return False
    
    for start_node in G.nodes:
        if backtrack(start_node, {start_node}):
            return True
    return False

# Generate a random graph
G = nx.gnm_random_graph(6, 9, seed=42)

# Check for Eulerian path in the original graph
has_eulerian_path = nx.has_eulerian_path(G)

# Generate the line graph of G
L_G = nx.line_graph(G)

# Check for Hamiltonian path in the line graph
has_hamiltonian_path = is_hamiltonian_path(L_G)

# Plot the graphs
fig, axes = plt.subplots(1, 2, figsize=(14, 7))

# Plot the original graph
nx.draw(G, with_labels=True, ax=axes[0])
axes[0].set_title(f"Original Graph\nEulerian Path: {has_eulerian_path}")

# Plot the line graph
nx.draw(L_G, with_labels=True, ax=axes[1])
axes[1].set_title(f"Line Graph\nHamiltonian Path: {has_hamiltonian_path}")

plt.show()

print(f"Eulerian Path: {has_eulerian_path}")
print(f"Hamiltonian Path: {has_hamiltonian_path}")
