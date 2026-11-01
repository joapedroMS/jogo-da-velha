'''
basicamente é uma matriz 3x3, o diferencial é que precisa do end="" para não quebrar a linha,
já que o print() por padrão quebra a linha. e o print() para quebrar a linha e ir para a 
proxima linha.
'''
def mostrar_tabuleiro(tabuleiro):
    for linha in range(3):
        for coluna in range(3):
            print(tabuleiro[linha][coluna], end="")

            if coluna < 2:
                print(" | ", end="")

        print()

        if linha < 2:
            print("--+---+--")
    return

tabuleiro =[
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]   
]
mostrar_tabuleiro(tabuleiro)