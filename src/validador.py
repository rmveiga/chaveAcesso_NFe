from src.util_nf import *
from src.chave_acesso import Chave_Acesso
import re


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


def valida_uf(cUF):
    if cUF in str(codigo_UF.keys()):
        return True
    return False


def valida_ano_mes(ano_mes):
    v = True
    ano_2d = str(ano_atual)[2:]
    mes_int = int(ano_mes[2:])
    if int(ano_mes[:2]) > int(ano_2d):
        v = False
    if mes_int not in range(1, 13):
        v = False

    return v


def valida_cnpj(cnpj):
    #  Verifica se o tipo do parâmetro é string
    if not isinstance(cnpj, str):
        return False

    #  Remove caracteres indesejáveis
    cnpj_ = re.sub("[^0-9]", '', cnpj)

    #  Verifica se o CNPJ possui 14 caracteres
    if len(cnpj_) != 14:
        return False

    sum = 0
    weight = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    """ Calcula o primeiro número do dígito verificador """
    for n in range(12):
        value = int(cnpj_[n]) * weight[n]
        sum = sum + value

    verifyingDigit = sum % 11

    if verifyingDigit < 2:
        firstVerifyingDigit = 0
    else:
        firstVerifyingDigit = 11 - verifyingDigit

    """ Calcula o segundo número do dígito verificador """
    sum = 0
    weight = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    for n in range(13):
        sum = sum + int(cnpj_[n]) * weight[n]

    verifyingDigit = sum % 11

    if verifyingDigit < 2:
        secondVerifyingDigit = 0
    else:
        secondVerifyingDigit = 11 - verifyingDigit

    if cnpj_[-2:] == "%s%s" % (firstVerifyingDigit, secondVerifyingDigit):
        return True
    return False


def valida_modeloNF(modelo):
    if modelo in str(modelo_nf.keys()):
        return True
    return False


def valida_tipo_emissao(tpEmis, modelo):
    # Verifica se o tipo de emissão está entre os tipos permitidos
    if int(tpEmis) not in tipo_emissao.keys():
        return False

    # Verifica se a contingência corresponde ao modelo da nota
    if int(tpEmis) != 1:
        if modelo == '65' and tpEmis not in '59':
            return False
    return True


def valida_digito_verificador(chave_sem_DV, cDV):
    pesos = [9, 8, 7, 6, 5, 4, 3, 2]
    temp = list()
    soma = 0

    # Percorre a chave de acesso sem o DV de traz pra frente
    for i in range(len(chave_sem_DV), 0, -1):
        if len(temp) == 0:
            temp = pesos[:]

        # Calcula a ponderação de cada dígito da chave de acesso e acumula a soma
        soma += int(chave_sem_DV[i - 1]) * temp[-1]
        del temp[-1]

    dv = 11 - (soma % 11)

    try:
        if dv == int(cDV):
            return True
        return False
    except:
        return False


def valida_chave_acesso(chave):
    chave_nfe = Chave_Acesso(chave)
    erros = list()
    valido = True
    while True:
        if not tamanho_chave_acesso(chave_nfe.chave):
            valido = False
            erros.append('O tamanho da chave de acesso está incorreto')
            break
        if not soh_numero(chave_nfe.chave):
            valido = False
            erros.append('A chave de acesso deve conter apenas números')
            break
        if not valida_uf(chave_nfe.cUF):
            valido = False
            erros.append('Código da UF inválido')
        if not valida_ano_mes(chave_nfe.AAMM):
            valido = False
            erros.append('Data de emissão inválida')
        if not valida_cnpj(chave_nfe.CNPJ):
            valido = False
            erros.append('CNPJ inválido')
        if not valida_modeloNF(chave_nfe.mod):
            valido = False
            erros.append('Modelo da nota diferente de 55: NF-e ou 65: NFC-e')
        if not valida_tipo_emissao(chave_nfe.tpEmis, chave_nfe.mod):
            valido = False
            erros.append('Tipo de contingência inválida para NFC-e')
        if not valida_digito_verificador(chave_nfe.chave_semDV, chave_nfe.cDV):
            valido = False
            erros.append('Dígito verificador inválido')
        break

    return valido, erros
