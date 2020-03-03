from src.validador import *

print('*' * 50)
print(f' {"VALIDAÇÃO DE CHAVE DE ACESSO NF-e":^50} ')
print('*' * 50)

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
