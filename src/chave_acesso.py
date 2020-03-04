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