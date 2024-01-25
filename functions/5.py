import random

def joga_craps():
    primeira_jogada = rolar_dados()
    print(f"Você rolou um total de {primeira_jogada}")

    if primeira_jogada in (7, 11):
        print("Natural! Você ganhou!")
    elif primeira_jogada in (2, 3, 12):
        print("Craps! Você perdeu.")
    else:
        ponto = primeira_jogada
        print(f"Seu ponto é {ponto}")
        continua_jogando(ponto)

def rolar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    total = dado1 + dado2
    return total

def continua_jogando(ponto):
    while True:
        jogada = rolar_dados()
        print(f"Você rolou um total de {jogada}")

        if jogada == ponto:
            print("Você fez o Ponto! Você ganhou!")
            break
        elif jogada == 7:
            print("Você tirou um 7. Você perdeu.")
            break

joga_craps()
