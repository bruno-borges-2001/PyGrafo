import sys

from representacao import Grafo
from A1.buscas import buscaEmLargura
from A1.cicloEuleriano import hierholzer
from A1.dijkstra import dijkstra
from A1.floydWarshall import floydWarshall

from A2.componentesFortementeConexas import componentesFortementeConexas
from A2.ordenacaoTopologica import ordenacaoTopologica
from A2.arvoreGeradoraMinima import kruskal

'''file = "tests/" + sys.argv[1] + ".net"'''

g = Grafo('tests/facebook_santiago.net')

print("busca em largura:")
buscaEmLargura(g, int(sys.argv[2]) if len(sys.argv) > 2 else 1)

print("ciclo euleriano")
hierholzer(g)

print("algoritmo de dijkstra")
dijkstra(g, int(sys.argv[2]) if len(sys.argv) > 2 else 1)

print("floyd warshall")
floydWarshall(g)

print("componentes fortemente conexas")
componentesFortementeConexas(g)

print("ordenacao topologica")
ordenacaoTopologica(g)

print("arvores geradoras minimas")
kruskal(g)
