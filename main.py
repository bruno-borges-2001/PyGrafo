from A2.arvoreGeradoraMinima import kruskal
from A2.ordenacaoTopologica import ordenacaoTopologica
from A2.componentesFortementeConexas import componentesFortementeConexas
from A1.floydWarshall import floydWarshall
from A1.dijkstra import dijkstra
from A1.cicloEuleriano import hierholzer
from A1.buscas import buscaEmLargura
from reader import readFile

from graph import NonDirectedGraph, DirectedGraph, BipartiteGraph

import sys
import os

g = BipartiteGraph('/tests/gr128_10.gr')

# while(1):

#     if (g is None):
#         try:
#             file = input('Digite o nome do arquivo a ser lido: ')

#             g = readFile('tests/' + file)
#             print(str(g))
#         except:
#             print('Erro ao carregar arquivo, tente novamente')
#             continue
#     os.system('clear')

#     directed = False

#     if isinstance(g, DirectedGraph):
#         directed = True

#     opt = input(
#         'Digite o número do algoritmo a ser executado:\n' +
#         '1 - ' + (('componentes fortemente conexas') if directed else ('busca em largura')) + '\n' +
#         '2 - ' + (('ordenacao topologica') if directed else ('ciclo euleriano')) + '\n' +
#         '3 - ' + (('arvores geradoras minimas') if directed else ('algoritmo de dijkstra')) + '\n' +
#         (('4 - floyd warshall\n') if not directed else ('')) +
#         '\n' +
#         '9 - trocar arquivo\n' +
#         '0 - sair\n'
#     )

#     os.system('clear')

#     if directed:
#         if (opt == '1'):
#             g.CFC()
#         if (opt == '2'):
#             g.TopologicalSort()
#     else:
#         if (opt == '1'):
#             g.BFS(1)
#         if (opt == '2'):
#             g.cicloEuleriano()
#         if (opt == '3'):
#             g.HamiltonianDijkstra(1)
#         if (opt == '4'):
#             g.HamiltonianFloydWarshall()
#     if (opt == '9'):
#         g = None
#         continue
#     if (opt == '0'):
#         break

#     input('\nTecle Enter para continuar...')
#     os.system('clear')

# print("componentes fortemente conexas")
# componentesFortementeConexas(g)

# print("ordenacao topologica")
# ordenacaoTopologica(g)

# print("arvores geradoras minimas")
# kruskal(g)
