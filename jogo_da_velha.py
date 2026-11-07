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
    
    diagonal_principal = True
    diagonal_secundaria = True

    for i in range(3):
        if tab[i][i] != jogador:
            diagonal_principal = False

        if tab[i][2 - i] != jogador:
            diagonal_secundaria = False

    if diagonal_principal or diagonal_secundaria:
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

def exibir_historico_e_placar(placar, historico_resultados):
    total_jogos = placar["X"] + placar["O"] + placar["Empates"]
    print("\n" + "=" * 40)
    print("          HISTORICO E PLACAR GERAL")
    print("=" * 40)
    print("Vitorias com peca X : " + str(placar["X"]))
    print("Vitorias com peca O : " + str(placar["O"]))
    print("Empates             : " + str(placar["Empates"]))
    print("Total de Partidas   : " + str(total_jogos))
    print("-" * 40)
    print("Historico de Partidas Realizadas:")
    if len(historico_resultados) == 0:
        print("  (Nenhuma partida concluida ate o momento)")
    else:
        for idx in range(len(historico_resultados)):
            print("  Rodada " + str(idx + 1) + ": " + historico_resultados[idx])
    print("=" * 40)
    input("\nPressione ENTER para voltar ao menu principal...")

def configurar_jogadores(modo):
    nome1 = input("\nNome do Jogador 1: ").strip()
    if nome1 == "":
        nome1 = "Jogador 1"

    if modo == "1":
        nome2 = input("Nome do Jogador 2: ").strip()
        if nome2 == "":
            nome2 = "Jogador 2"
    else:
        nome2 = "Computador"

    simbolo1 = ""
    while simbolo1 != "X" and simbolo1 != "O":
        simbolo1 = input(nome1 + ", escolha seu simbolo (X ou O): ").strip().upper()
        if simbolo1 != "X" and simbolo1 != "O":
            print("Opcao invalida! Digite apenas X ou O.")

    if simbolo1 == "X":
        simbolo2 = "O"
    else:
        simbolo2 = "X"

    print("\n[Confirmacao de Jogadores]")
    print(nome1 + " -> Simbolo: " + simbolo1)
    print(nome2 + " -> Simbolo: " + simbolo2)

    return ((nome1, simbolo1), (nome2, simbolo2))

def executar_partidas(placar, historico_resultados):
    print("\n--- ESCOLHA DO MODO DE DISPUTA ---")
    print("1 - Jogador vs Jogador")
    print("2 - Jogador vs Maquina")

    modo = ""
    while modo != "1" and modo != "2":
        modo = input("Selecione o modo (1 ou 2): ").strip()
        if modo != "1" and modo != "2":
            print("Opcao invalida! Digite 1 ou 2.")

    jogador1, jogador2 = configurar_jogadores(modo)
    nome1, simb1 = jogador1[0], jogador1[1]
    nome2, simb2 = jogador2[0], jogador2[1]

    em_jogo = True
    while em_jogo:
        tabuleiro = criar_tabuleiro()
        posicoes_ocupadas = set()
        turno_j1 = True
        partida_ativa = True

        while partida_ativa:
            exibir_tabuleiro(tabuleiro)

            if turno_j1:
                pos = ler_coordenada(tabuleiro, posicoes_ocupadas, nome1, simb1)
                tabuleiro[pos[0]][pos[1]] = simb1
                posicoes_ocupadas.add(pos)

                if verificar_vitoria(tabuleiro, simb1):
                    exibir_tabuleiro(tabuleiro)
                    print("Vitoria de " + nome1 + " (" + simb1 + ")!")
                    placar[simb1] = placar[simb1] + 1
                    historico_resultados.append(nome1 + " (" + simb1 + ") venceu")
                    partida_ativa = False
            else:
                if modo == "1":
                    pos = ler_coordenada(tabuleiro, posicoes_ocupadas, nome2, simb2)
                else:
                    print("Computador realizando jogada...")
                    pos = jogada_maquina(tabuleiro, simb2, simb1)

                tabuleiro[pos[0]][pos[1]] = simb2
                posicoes_ocupadas.add(pos)

                if verificar_vitoria(tabuleiro, simb2):
                    exibir_tabuleiro(tabuleiro)
                    print("Vitoria de " + nome2 + " (" + simb2 + ")!")
                    placar[simb2] = placar[simb2] + 1
                    historico_resultados.append(nome2 + " (" + simb2 + ") venceu")
                    partida_ativa = False

            if partida_ativa and len(obter_posicoes_vazias(tabuleiro)) == 0:
                exibir_tabuleiro(tabuleiro)
                print("Partida empatada (Deu Velha)!")
                placar["Empates"] = placar["Empates"] + 1
                historico_resultados.append("Empate")
                partida_ativa = False

            turno_j1 = not turno_j1

        while True:
            resp = input("\nDesejam disputar mais uma partida com estes mesmos jogadores? (S/N): ").strip().upper()
            if resp == "S":
                break
            elif resp == "N":
                em_jogo = False
                break
            else:
                print("Opcao invalida. Digite apenas S ou N.")

def main():
    placar = {"X": 0, "O": 0, "Empates": 0}
    historico_resultados = []

    executando = True
    while executando:
        print("\n" + "#" * 38)
        print("          JOGO DA VELHA EM PYTHON")
        print("#" * 38)
        print(" [1] Iniciar Partida")
        print(" [2] Ver Regras do Jogo")
        print(" [3] Ver Historico e Placar Geral")
        print(" [0] Encerrar Programa")
        print("#" * 38)

        opcao = input("Digite a opcao desejada: ").strip()

        if opcao == "1":
            executar_partidas(placar, historico_resultados)
        elif opcao == "2":
            exibir_regras()
        elif opcao == "3":
            exibir_historico_e_placar(placar, historico_resultados)
        elif opcao == "0":
            print("\nEncerrando o programa. Obrigado por jogar!")
            executando = False
        else:
            print("Opcao inexistente! Digite 1, 2, 3 ou 0.")


if __name__ == "__main__":
    main()