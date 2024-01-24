vetor1 = []
vetor2 = []

print("Digite os elementos do primeiro vetor:")
for i in range(5):
    elemento = int(input(f"Digite o {i + 1}º elemento: "))
    vetor1.append(elemento)

print("\nDigite os elementos do segundo vetor:")
for i in range(5):
    elemento = int(input(f"Digite o {i + 1}º elemento: "))
    vetor2.append(elemento)

vetor3 = sorted(vetor1 + vetor2)

print("\nTerceiro vetor composto pelos elementos em ordem crescente:")
print(vetor3)
