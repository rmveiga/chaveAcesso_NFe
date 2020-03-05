from src.util_nf import *


class Chave_Acesso:

    def __init__(self, chave):
        self.cUF = chave[:2]
        self.AAMM = chave[2:6]
        self.CNPJ = chave[6:20]
        self.mod = chave[20:22]
        self.serie = chave[22:25]
        self.nNF = chave[25:34]
        self.tpEmis = chave[34:35]
        self.cNF = chave[35:43]
        self.cDV = chave[43:44]
        self.chave = chave
        self.chave_semDV = chave[:43]

    def codigo_UF(self):
        return codigo_UF[int(self.cUF)]

    def ano_mes(self):
        return f'{meses[int(self.AAMM[2:4])]}/20{self.AAMM[:2]}'

    def cnpj(self):
        return f'{self.CNPJ[:2]}.{self.CNPJ[2:5]}.{self.CNPJ[5:8]}/{self.CNPJ[8:12]}-{self.CNPJ[12:14]}'

    def modelo(self):
        return modelo_nf[int(self.mod)]

    def tipo_emissao(self):
        return tipo_emissao[int(self.tpEmis)]
