import sys

from representacao import Grafo
from buscas import buscaEmLargura
from cicloEuleriano import hierholzer
from dijkstra import dijkstra

file = "tests/" + sys.argv[1] + ".net"

g = Grafo(file)

print("busca em largura:")
buscaEmLargura(g, int(sys.argv[2]) if len(sys.argv) > 2 else 1)
print("ciclo euleriano")
hierholzer(g)
print("algoritmo de dijkstra")
dijkstra(g, int(sys.argv[2]) if len(sys.argv) > 2 else 1)
