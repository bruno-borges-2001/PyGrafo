from A2.arvoreGeradoraMinima import kruskal
from A2.ordenacaoTopologica import ordenacaoTopologica
from A2.componentesFortementeConexas import componentesFortementeConexas
from A1.floydWarshall import floydWarshall
from A1.dijkstra import dijkstra
from A1.cicloEuleriano import hierholzer
from A1.buscas import buscaEmLargura
import sys
from reader import readFile

g = None

while(1):

    if (g is None):
        '''try:'''
        file = input('Digite o nome do arquivo a ser lido: ')

        g = readFile('tests/' + file)
        print(str(g))
        '''except:
            print('Erro ao carregar arquivo, tente novamente')
            continue
        '''

    opt = input(
        'Digite o número do algoritmo a ser executado:\n' +
        '1 - busca em largura:\n' +
        '2 - ciclo euleriano\n' +
        '3 - algoritmo de dijkstra\n' +
        '4 - floyd warshall\n' +
        '\n9 - trocar arquivo\n' +
        '0 - sair\n\n'
    )
    if (opt == '1'):
        g.BFS(1)
    if (opt == '2'):
        g.cicloEuleriano()
    if (opt == '3'):
        g.HamiltonianDijkstra(1)
    if (opt == '4'):
        g.HamiltonianFloydWarshall()
    if (opt == '9'):
        g = None
    if (opt == '0'):
        break

    input('\nTecle Enter para continuar...')

# print("componentes fortemente conexas")
# componentesFortementeConexas(g)

# print("ordenacao topologica")
# ordenacaoTopologica(g)

# print("arvores geradoras minimas")
# kruskal(g)
