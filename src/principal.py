from src.validador import valida_chave_acesso
from src.util import *

print('*' * 75)
print(f' {"VALIDAÇÃO DE CHAVE DE ACESSO NF-e":^75} ')
print('*' * 75)

while True:
    chave_acesso = str(input('Informe a chave de acesso: ')).strip()
    resultado, lista_erros, chave_nf = valida_chave_acesso(chave_acesso)

    if resultado:
        print('CHAVE DE ACESSO VÁLIDA')
        print('-' * 75)
        print(f'UF de emissão: {chave_nf.codigo_UF()}')
        print(f'Data de emissão: {chave_nf.ano_mes()}')
        print(f'CNPJ do emissor: {chave_nf.cnpj()}')
        print(f'Modelo da Nota Fiscal: {chave_nf.modelo()}')
        print(f'Série: {chave_nf.serie}')
        print(f'Número: {chave_nf.nNF}')
        print(f'Tipo de emissão: {chave_nf.tipo_emissao()}')
    else:
        print('CHAVE DE ACESSO INÁLIDA')
        print('*' * 75)
        print(f' {"LISTAGEM DE ERROS":^75} ')
        print('*' * 75)
        for erro in lista_erros:
            print(erro)
    print('-' * 75)

    opcao = str(input('Deseja validar outra chave de acesso? [S/N] ')).strip().upper()[0]
    while opcao not in 'SN':
        msg_erro('Opção inválida')
        opcao = str(input('Deseja validar outra chave de acesso? [S/N] ')).strip().upper()[0]

    if opcao == 'N':
        break