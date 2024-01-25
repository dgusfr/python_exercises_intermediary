def reverso_numero(numero):
    reverso = int(str(numero)[::-1])
    return reverso

numero_informado = int(input("Informe um número inteiro: "))

resultado = reverso_numero(numero_informado)
print(f"O reverso do número {numero_informado} é: {resultado}")
