def criar_tabuleiro():
    tabuleiro = []
    for i in range(3):
        linha = []
        for j in range(3):
            linha.append(" ")
        tabuleiro.append(linha)
    return tabuleiro

