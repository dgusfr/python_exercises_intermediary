import random

def lancar_dado():
    return random.randint(1, 6)

contadores = [0] * 6

for _ in range(100):
    resultado = lancar_dado()
    contadores[resultado - 1] += 1

print("Resultados dos lançamentos:")
for i in range(6):
    print(f"Face {i + 1}: {contadores[i]} vezes")
