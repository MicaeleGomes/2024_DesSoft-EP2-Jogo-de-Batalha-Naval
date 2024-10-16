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