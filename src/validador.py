numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
erros = list()
cUF = {
    # REGIÃO NORTE
    11: 'Rondônia',
    12: 'Acre',
    13: 'Amazonas',
    14: 'Roraima',
    15: 'Pará',
    16: 'Amapá',
    17: 'Tocantins',
    #  REGIÃO NORDESTE
    21: 'Maranhão',
    22: 'Piauí',
    23: 'Ceará',
    24: 'Rio Grande do Norte',
    25: 'Paraíba',
    26: 'Pernambuco',
    27: 'Alagoas',
    28: 'Sergipe',
    29: 'Bahia',
    #  REGIÃO SUDESTE
    31: 'Minas Gerais',
    32: 'Espírito Santo',
    33: 'Rio de Janeiro',
    34: 'São Paulo',
    #  REGIÃO SUL
    41: 'Paraná',
    42: 'Santa Catarina',
    43: 'Rio Grande do Sul',
    #  REGIÃO CENTRO-OESTE
    50: 'Mato Grosso do Sul',
    51: 'Mato Grosso',
    52: 'Goiás',
    53: 'Distrito Federal'}


def tamanho_chave_acesso(chave):
    if len(chave) == 44:
        return True
    else:
        return False


def soh_numero(chave):
    v = True
    for i in chave:
        if i not in str(numeros):
            v = False

    return v


def valida_uf(cod_uf):
    if cod_uf in str(cUF.keys()):
        return True
    else:
        return False


def valida_chave_acesso(chave_acesso):
    valido = True
    if not tamanho_chave_acesso(chave_acesso):
        valido = False
        erros.append('O tamanho da chave de acesso está incorreto')
    if not soh_numero(chave_acesso):
        valido = False
        erros.append('A chave de acesso deve conter apenas números')
    if not valida_uf(chave_acesso[:2]):
        valido = False
        erros.append('Código da UF inválido')

    return valido, erros
