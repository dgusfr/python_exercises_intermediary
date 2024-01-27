import random

def escolher_palavra():
    # Lista de palavras para o jogo
    palavras = ['ABACAXI', 'BANANA', 'CACHORRO', 'GATO', 'ELEFANTE', 'GIRASSOL', 'PAPAGAIO', 'MORANGO']
    # Escolhe uma palavra aleatoriamente da lista
    return random.choice(palavras)

def exibir_palavra_secreta(palavra, letras_certas):
    # Exibe a palavra secreta substituindo letras não reveladas por '_'
    palavra_secreta = ''
    for letra in palavra:
        if letra in letras_certas:
            palavra_secreta += letra + ' '
        else:
            palavra_secreta += '_ '
    return palavra_secreta.strip()

def jogar_forca():
    palavra = escolher_palavra()
    letras_certas = set()
    tentativas = 0

    print("Bem-vindo ao jogo da Forca!")
    print("Tente adivinhar a palavra secreta.")

    while True:
        print("\nPalavra:", exibir_palavra_secreta(palavra, letras_certas))

        letra = input("Digite uma letra: ").upper()

        if letra in palavra:
            letras_certas.add(letra)
            print("Letra correta!")

            # Verifica se o jogador acertou todas as letras da palavra
            if set(palavra) == letras_certas:
                print("\nParabéns! Você venceu! A palavra era:", palavra)
                break
        else:
            tentativas += 1
            print(f"\n-> Você errou pela {tentativas}ª vez. Tente de novo!")

            # Verifica se o jogador atingiu o limite de tentativas
            if tentativas == 6:
                print("\nVocê foi enforcado! A palavra era:", palavra)
                break

# Chama a função para iniciar o jogo
jogar_forca()
