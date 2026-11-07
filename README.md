# 🎮 Jogo da Velha em Python

## 📌 Sobre o projeto

Este projeto consiste no desenvolvimento de um jogo da velha utilizando a linguagem de programação Python. O programa funciona pelo terminal e permite que os usuários disputem partidas entre si ou contra o computador.

O objetivo do projeto é aplicar conceitos fundamentais de programação, como funções, estruturas condicionais, estruturas de repetição, listas, matrizes, tuplas e manipulação de dados.

**Integrantes:**
- Emanuel Barbosa Silva
- João Pedro Moura Soares

## 🚀 Como executar o programa

### Pré-requisitos

- Ter o Python 3 instalado no computador.
- Ter acesso a um terminal ou editor de código, como Visual Studio Code.

### Passo a passo

**1. Clone o repositório:**

```bash
git clone https://github.com/joapedroMS/jogo-da-velha.git
```

**2. Acesse a pasta do projeto:**

```bash
cd jogo-da-velha
```

**3. Execute o programa:**

```bash
python jogo_da_velha.py
```

Caso o comando anterior não funcione, tente:

```bash
python3 jogo_da_velha.py
```

Não é necessário instalar bibliotecas externas, pois o programa utiliza recursos nativos do Python.

## 📖 Regras do jogo

O jogo acontece em um tabuleiro de 3 linhas por 3 colunas, no qual os jogadores utilizam os símbolos X e O.

### Como jogar

1. Escolha o modo de disputa: jogador contra jogador ou jogador contra máquina.
2. Informe o nome dos jogadores.
3. Escolha o símbolo X ou O.
4. Os jogadores devem alternar suas jogadas.
5. Para realizar uma jogada, informe o número da linha e da coluna desejadas.

**Exemplo:** para marcar a posição central do tabuleiro, informe:

```text
2 2
```

### Condições de vitória

Vence o jogador que conseguir alinhar três símbolos iguais:

- **Horizontalmente:** três símbolos na mesma linha.
- **Verticalmente:** três símbolos na mesma coluna.
- **Diagonalmente:** três símbolos em uma das diagonais.

### Empate

Caso todas as nove posições sejam preenchidas e nenhum jogador consiga formar uma sequência de três símbolos iguais, a partida termina em empate, conhecido como "Deu Velha".

## 🏆 Desafios e funcionalidades implementadas


### 1. Modo jogador contra jogador

Permite que duas pessoas disputem uma partida no mesmo computador, alternando suas jogadas até que alguém vença ou ocorra um empate.

### 2. Modo jogador contra máquina

Implementa um adversário controlado pelo computador, que utiliza uma lógica de decisão para escolher suas jogadas.

A máquina segue prioridades para definir suas ações:

- Verifica se existe uma jogada que garanta sua vitória.
- Identifica se o adversário está prestes a vencer e tenta bloquear sua jogada.
- Prioriza a posição central do tabuleiro.
- Procura ocupar uma das posições dos cantos.
- Caso as opções anteriores não estejam disponíveis, escolhe uma posição livre.

### 3. Validação das jogadas

O programa verifica se as coordenadas informadas são válidas, impedindo que o jogador:

- Digite valores diferentes de números inteiros.
- Informe posições fora do tabuleiro.
- Escolha uma posição que já esteja ocupada.
- Informe as coordenadas em formato incorreto.

### 4. Sistema de pontuação e histórico

O programa mantém um placar geral durante sua execução, contabilizando:

- Vitórias com o símbolo X.
- Vitórias com o símbolo O.
- Quantidade de empates.
- Total de partidas realizadas.

Também registra os resultados das partidas concluídas, permitindo consultar o histórico posteriormente.

### 5. Menu interativo e revanche

O programa apresenta um menu principal com opções para:

- Iniciar uma partida.
- Consultar as regras.
- Consultar o histórico e o placar geral.
- Encerrar o programa.

Após uma partida, os jogadores podem escolher se desejam disputar outra rodada.

## ⚙️ Funções criadas e suas responsabilidades

O código foi organizado em funções para dividir as responsabilidades do programa, facilitar a compreensão e evitar a repetição desnecessária de instruções.

As funções foram desenvolvidas e distribuídas entre os dois integrantes da equipe.

### 👨‍💻 Emanuel Barbosa Silva

| Função | Responsabilidade |
|---|---|
| `exibir_tabuleiro()` | Exibir o tabuleiro no terminal, com suas posições organizadas em uma estrutura 3x3. |
| `ler_coordenada()` | Receber, validar e verificar as coordenadas informadas pelo jogador. |
| `jogada_maquina()` | Implementar a lógica determinística do computador, analisando as jogadas do adversário para decidir sua próxima ação. |
| `configurar_jogadores()` | Realizar o cadastro dos nomes dos jogadores e a definição dos símbolos utilizados na partida. |
| `main()` | Organizar a estrutura do menu principal e controlar as opções disponíveis ao usuário. |

### 👨‍💻 João Pedro Moura Soares

| Função | Responsabilidade |
|---|---|
| `criar_tabuleiro()` | Criar e inicializar a matriz 3x3 que representa o tabuleiro. |
| `verificar_vitoria()` | Verificar se existe uma combinação vencedora nas linhas, colunas ou diagonais. |
| `exibir_regras()` | Elaborar e apresentar a tela com as regras e instruções do jogo. |
| `exibir_historico_e_placar()` | Exibir o placar geral e o histórico das partidas realizadas. |
| `executar_partidas()` | Controlar o ciclo das partidas, o andamento das jogadas e os modos de jogo. |

## 📝 Exemplos de commits e contribuições

Os commits registram as alterações e funcionalidades implementadas durante o desenvolvimento do projeto, permitindo acompanhar a evolução do código e a contribuição de cada integrante.

### Emanuel Barbosa Silva

- Implementação do funcionamento do tabuleiro no terminal, com posições em 3x3.
- Verificação de posições vazias e validação das coordenadas.
- Validação e verificação das respostas dos jogadores.
- Implementação das jogadas da máquina após análise do comportamento do jogador humano.
- Personalização dos jogadores e registro de seus nomes e símbolos.
- Armazenamento do placar e execução do menu principal.

### João Pedro Moura Soares

- Criação e atualização do tabuleiro em uma estrutura de matriz 3x3.
- Implementação da função de verificação de vitória utilizando estruturas condicionais (`for` e `if`).
- Criação da função para mostrar as regras do jogo no menu.
- Implementação da exibição do histórico e placar das partidas.
- Desenvolvimento do controle de execução das partidas e dos modos de jogo.

## 🧠 Conceitos de programação utilizados

Durante a construção do projeto, foram utilizados os seguintes conceitos:

- **Variáveis:** armazenamento de nomes, símbolos, pontuações e estados do jogo.
- **Listas e matrizes:** representação e manipulação do tabuleiro.
- **Tuplas:** armazenamento de coordenadas das posições.
- **Conjuntos (set):** controle das posições ocupadas.
- **Estruturas condicionais (`if`, `elif` e `else`):** tomada de decisões durante o jogo.
- **Estruturas de repetição (`for` e `while`):** controle das jogadas, validações e funcionamento dos menus.
- **Funções:** organização e reutilização do código.
- **Dicionários:** armazenamento da pontuação geral.
- **Manipulação de strings:** tratamento e validação das entradas dos usuários.

## 📁 Estrutura do projeto

```text
jogo-da-velha/
│
├── jogo_da_velha.py
│
└── README.md
```
