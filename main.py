import pandas as pd
import networkx as nx
import json

# função principal 
def main():
    print('BEM-VINDO A O FIFA-GRAPH-ANALYZER\n')
    print('CARREGANDO O GRAFO...') 
    # carrega o grafo a partir do arquivo gml
    G = nx.read_gml('grafo.gml')
    print('GRAFO CARREGADO  COM SUCESSO!\n\n')
    print('OBS: PARA SAIR DIGITE exit')
    print('Digite o nome de dois jogadores que não atuaram juntos durante a carreira: ')
    jogador1 = 'null' 
    # enquanto o usuário não sair
    while(jogador1 != 'exit'): 
        # recebe um jogador
        jogador1 = input('Digite o nome do primeiro jogador: ')
        if(jogador1 != 'exit'):
            if(G.has_node(jogador1)):
                print('JOGADOR ENCONTRADO NO GRAFO!') 
                # se achou o primeiro jogador então procura o segundo
                jogador2 = input('Digite o nome do segundo jogador: ')
                if(jogador2 != 'exit'):
                    if(G.has_node(jogador2)):
                        print('JOGADOR ENCONTRADO NO GRAFO!\n') 
                        # com os dois jogadores encontrados pode se encontrar o caminho minimo entre eles
                        caminhoMinimo(jogador1, jogador2, G)

                    else:
                        print('JOGADOR NÃO ENCONTRADO, POR FAVOR, VERIFICAR SE O NOME ESTÁ CORRETO')
            else:
                print('JOGADOR NÃO ENCONTRADO, POR FAVOR, VERIFICAR SE O NOME ESTÁ CORRETO')
 
# funcao para o caminho minimo com complexidade V+E 
def caminhoMinimo(player1, player2, grafo):
    try:
        caminho = nx.shortest_path(grafo, player1, player2)
        print('A distância mínima é ', len(caminho)-1)
        print('O caminho percorrido foi: ')
        for sp in caminho:
            print(sp,'\n')
    except: 
        # se os jogadores não possuem um caminho entre si 
        print('OS JOGADORES NÃO POSSUEM NENHUMA LIGAÇÃO\n')

main()