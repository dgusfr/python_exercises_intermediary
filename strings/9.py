def validar_e_corrigir_telefone(telefone):
    # Remove caracteres não numéricos do telefone
    telefone_numerico = ''.join(filter(str.isdigit, telefone))

    # Verifica se o telefone tem apenas 7 dígitos
    if len(telefone_numerico) == 7:
        telefone_corrigido = '3' + telefone_numerico
        return telefone_corrigido
    # Se o telefone tiver 10 dígitos (com traço), remove o traço e retorna o telefone formatado
    elif len(telefone_numerico) == 10:
        telefone_corrigido = '3' + telefone_numerico[1:]
        return telefone_corrigido
    else:
        return None

# Solicita ao usuário que digite o número de telefone
telefone = input("Telefone: ")

# Chama a função para validar e corrigir o número de telefone
telefone_corrigido = validar_e_corrigir_telefone(telefone)

# Verifica se o número de telefone foi corrigido com sucesso
if telefone_corrigido:
    if len(telefone_corrigido) == 8:
        print("Telefone possui 7 dígitos. Acrescentarei o dígito três na frente.")
    else:
        print("Telefone já possui 8 dígitos.")

    # Exibe o telefone corrigido sem formatação
    print("Telefone corrigido sem formatação:", telefone_corrigido)

    # Exibe o telefone corrigido com formatação
    telefone_formatado = telefone_corrigido[:4] + '-' + telefone_corrigido[4:]
    print("Telefone corrigido com formatação:", telefone_formatado)
else:
    print("Número de telefone inválido.")
