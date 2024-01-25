def contar_digitos(numero):
    quantidade_digitos = len(str(numero))
    return quantidade_digitos

numero_informado = int(input("Informe um número inteiro: "))

resultado = contar_digitos(numero_informado)
print(f"O número {numero_informado} possui {resultado} dígitos.")
