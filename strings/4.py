def imprimir_escada(nome):
    for i in range(1, len(nome) + 1):
        print(nome[:i].upper())

# Solicita ao usuário que digite o nome
nome = input("Digite seu nome: ")

# Chama a função para imprimir o nome em formato de escada
imprimir_escada(nome)
