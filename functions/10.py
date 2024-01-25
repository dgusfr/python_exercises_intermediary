def encontrar_fatorial(numero):
    fatorial = 1
    i = 1

    # Encontrar o fatorial enquanto for menor que o número
    while fatorial < numero:
        i += 1
        fatorial *= i

    # Verificar se o número é igual ao fatorial encontrado
    if fatorial == numero:
        print(f"{numero} = {i}!")
    else:
        print(f"{i - 1}! < {numero} < {i}!")

# Solicitar entrada do usuário
numero_input = int(input("Digite um número inteiro positivo: "))

# Chamar a função e imprimir o resultado
encontrar_fatorial(numero_input)
