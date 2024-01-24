# Criando um vetor de 10 números reais
vetor = []

# Lendo os números do usuário e adicionando ao vetor
for i in range(10):
    numero = float(input(f"Digite o {i + 1}º número real: "))
    vetor.append(numero)

# Mostrando os números na ordem inversa
print("Números na ordem inversa:")
for num in reversed(vetor):
    print(num)

# Mostrando os números na ordem inversa sem usar reversed
print("Números na ordem inversa:")
for i in range(9, -1, -1):
    print(vetor[i])