import sys

from representacao import Grafo
from buscas import buscaEmLargura
from cicloEuleriano import hierholzer
from dijkstra import dijkstra
from floydWarshall import floydWarshall

'''file = "tests/" + sys.argv[1] + ".net"'''

g = Grafo('tests/ContemCicloEuleriano.net')
dijkstra(g, 1)

'''
print("busca em largura:")
buscaEmLargura(g, int(sys.argv[2]) if len(sys.argv) > 2 else 1)
print("ciclo euleriano")
hierholzer(g)
print("algoritmo de dijkstra")
dijkstra(g, int(sys.argv[2]) if len(sys.argv) > 2 else 1)
'''