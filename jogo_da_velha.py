def criar_tabuleiro():
    tabuleiro = []
    for i in range(3):
        linha = []
        for j in range(3):
            linha.append(" ")
        tabuleiro.append(linha)
    return tabuleiro

def exibir_tabuleiro(tab):
    print()
    print("    1   2   3")
    print("  +---+---+---+")
    for i in range(3):
        linha_str = str(i + 1) + " |"
        for j in range(3):
            linha_str = linha_str + " " + tab[i][j] + " |"
        print(linha_str)
        print("  +---+---+---+")
    print()

def verificar_vitoria(tab, jogador):
    for i in range(3):
        if tab[i][0] == jogador and tab[i][1] == jogador and tab[i][2] == jogador:
            return True
        if tab[0][i] == jogador and tab[1][i] == jogador and tab[2][i] == jogador:
            return True

    if tab[0][0] == jogador and tab[1][1] == jogador and tab[2][2] == jogador:
        return True
    if tab[0][2] == jogador and tab[1][1] == jogador and tab[2][0] == jogador:
        return True

    return False
