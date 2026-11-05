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

def obter_posicoes_vazias(tab):
    vazias = []
    for l in range(3):
        for c in range(3):
            if tab[l][c] == " ":
                vazias.append((l, c))
    return vazias

def ler_coordenada(tab, posicoes_ocupadas_set, nome, simbolo):
    while True:
        entrada = input(nome + " (" + simbolo + "), digite linha e coluna (ex: 1 2): ").strip()
        partes = entrada.split()

        if len(partes) == 2:
            if partes[0].isdigit() and partes[1].isdigit():
                l = int(partes[0]) - 1
                c = int(partes[1]) - 1

                if (0 <= l <= 2) and (0 <= c <= 2):
                    pos = (l, c)
                    if pos in posicoes_ocupadas_set:
                        print("Essa casa ja esta ocupada! Escolha outra.")
                    else:
                        return pos
                else:
                    print("Valores fora da grade! Digite numeros de 1 a 3.")
            else:
                print("Entrada invalida! Digite apenas numeros inteiros.")
        else:
            print("Formato incorreto! Digite dois numeros separados por espaco.")

def jogada_maquina(tab, simbolo_maquina, simbolo_humano):
    livres = obter_posicoes_vazias(tab)

    for l, c in livres:
        tab[l][c] = simbolo_maquina
        if verificar_vitoria(tab, simbolo_maquina):
            tab[l][c] = " "
            return (l, c)
        tab[l][c] = " "

    for l, c in livres:
        tab[l][c] = simbolo_humano
        if verificar_vitoria(tab, simbolo_humano):
            tab[l][c] = " "
            return (l, c)
        tab[l][c] = " "

    if tab[1][1] == " ":
        return (1, 1)


    cantos = ((0, 0), (0, 2), (2, 0), (2, 2))
    for l, c in cantos:
        if (l, c) in livres:
            return (l, c)

    return livres[0]

def exibir_regras():
    print("\n" + "=" * 45)
    print("            REGRAS DO JOGO DA VELHA")
    print("=" * 45)
    print("1. O jogo ocorre em uma grade de 3 linhas por 3 colunas.")
    print("2. Dois jogadores alternam jogadas marcando casas vazias.")
    print("3. Como jogar: Digite o numero da LINHA seguido")
    print("   do numero da COLUNA separados por espaco (ex: 2 2).")
    print("4. Linhas vao de 1 a 3 (cima para baixo).")
    print("5. Colunas vao de 1 a 3 (esquerda para a direita).")
    print("6. Vence quem alinhar 3 pecas na horizontal,")
    print("   vertical ou diagonal primeiro.")
    print("7. Se todas as 9 casas forem preenchidas sem trinca,")
    print("   a partida termina em empate ('Deu Velha').")
    print("=" * 45)
    input("\nPressione ENTER para voltar ao menu principal...")
    