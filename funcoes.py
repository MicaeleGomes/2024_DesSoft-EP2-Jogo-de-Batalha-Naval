def define_posicoes(linha, coluna, orientacao, tamanho): 

    lista_posicoes = []

    if orientacao == 'vertical':

        for i in range(tamanho):

            nova_linha = linha + i
            listinha = [nova_linha, coluna]
            lista_posicoes.append(listinha)


    elif orientacao == 'horizontal':
        for i in range(tamanho):
            nova_coluna = coluna + i
            listinha = [linha, nova_coluna]
            lista_posicoes.append(listinha)


    return lista_posicoes


def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):

    posicoes_navio = define_posicoes(linha, coluna, orientacao, tamanho)

    if nome_navio in frota:

        frota[nome_navio].append(posicoes_navio)

    else:
        frota[nome_navio] = [posicoes_navio]
        
    return frota

def faz_jogada(tabuleiro, linha, coluna):

    if tabuleiro[linha][coluna] == 1: 
        tabuleiro[linha][coluna] = 'X' 

    else: 
        tabuleiro[linha][coluna] = '-' 

    return tabuleiro


def posiciona_frota(frota): 

    grid = [[0 for _ in range(10)] for _ in range(10)]

    for navio in frota:
        lista_posicoes = frota[navio]
        for posicoes_navio in lista_posicoes:
            for posicao in posicoes_navio:
                linha = posicao[0]
                coluna = posicao[1]
                grid[linha][coluna] = 1

    return grid
