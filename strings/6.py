def contar_espacos(frase):
    total_espacos = frase.count(' ')
    return total_espacos

frase = "Dado uma string com uma frase conte quantos espaços em branco existem na frase."
total_espacos = contar_espacos(frase)

print("Total de espaços em branco na frase:", total_espacos)

