from src.validador import valida_chave_acesso
from src.util import *

print('*' * 50)
print(f' {"VALIDAÇÃO DE CHAVE DE ACESSO NF-e":^50} ')
print('*' * 50)

while True:
    chave_acesso = str(input('Informe a chave de acesso: ')).strip()
    resultado, lista_erros = valida_chave_acesso(chave_acesso)

    if resultado:
        print('CHAVE DE ACESSO VÁLIDA')
    else:
        print('CHAVE DE ACESSO INÁLIDA')
        print('*' * 50)
        print(f' {"LISTAGEM DE ERROS":^50} ')
        print('*' * 50)
        for erro in lista_erros:
            print(erro)
    print('-' * 50)

    opcao = str(input('Deseja validar outra chave de acesso? [S/N] ')).strip().upper()[0]
    while opcao not in 'SN':
        msg_erro('Opção inválida')
        opcao = str(input('Deseja validar outra chave de acesso? [S/N] ')).strip().upper()[0]

    if opcao == 'N':
        break