meuVetor = [1, 2, 3, 4, 5]
print(meuVetor)

#Com entrada do usuario:

vetor = []

# Lendo os números do usuário e adicionando ao vetor
for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    vetor.append(numero)

# Mostrando os números do vetor
print("Números no vetor:")
for num in vetor:
    print(num)
