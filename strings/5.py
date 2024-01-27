def imprimir_escada_invertida(nome):
    for i in range(len(nome), 0, -1):
        # (Tamanho Intervalo, valor Final Intervalo, Decremento)
        print(nome[:i].upper())
        # Imprime uma fatia do nome, começando do índice 0 até 'i' (não inclusivo),

nome = input("Digite seu nome: ")
imprimir_escada_invertida(nome)