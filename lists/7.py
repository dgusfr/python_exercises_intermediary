vetor = []

for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número inteiro para o vetor A: "))
    vetor.append(numero)

soma_quadrados = sum(num ** 2 for num in vetor)

print(f"\nA soma dos quadrados dos elementos do vetor A é: {soma_quadrados}")
