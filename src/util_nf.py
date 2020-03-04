from datetime import date

ano_atual = date.today().year
mes_atual = date.today().month

numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
codigo_UF = {
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

modelo_nf = {55: 'NF-e',
             65: 'NFC-e'}


#  Para a NFC-e somente estão disponíveis e são válidas as opções de contingência 5 e 9.
tipo_emissao = {1: 'Emissão normal (não em contingência)',
                2: 'Contingência FS-IA, com impressão do DANFE em formulário de segurança',
                3: 'Contingência SCAN (Sistema de Contingência do Ambiente Nacional)',
                4: 'Contingência DPEC (Declaração Prévia da Emissão em Contingência)',
                5: 'Contingência FS-DA, com impressão do DANFE em formulário de segurança',
                6: 'Contingência SVC-AN (SEFAZ Virtual de Contingência do AN)',
                7: 'Contingência SVC-RS (SEFAZ Virtual de Contingência do RS)',
                9: 'Contingência off-line da NFC-e (as demais opções de contingência são válidas também para a NFC-e)'}

