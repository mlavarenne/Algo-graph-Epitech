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


positions = [3, 7, 2, 5, 9]
ordre = [2, 5, 3, 7, 9]

print("tri_positions")
print(tri_positions(positions))

positions = [3, 7, 2, 5, 9]
ordre = [2, 5, 3, 7, 9]

print("glouton")
print(glouton(positions))

positions = [3, 7, 2, 5, 9]
ordre = [2, 5, 3, 7, 9]

print("temps_attente_moyen")
print(temps_attente_moyen(positions, ordre))