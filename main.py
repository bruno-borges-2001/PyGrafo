import sys

from representacao import Grafo
from buscas import buscaEmLargura
from cicloEuleriano import hierholzer
from dijkstra import dijkstra

file = "tests/" + sys.argv[1] + ".net"
print(file)

g = Grafo(file)

print("busca em largura:")
buscaEmLargura(g, 1)
print("ciclo euleriano")
hierholzer(g)
print("algoritmo de dijkstra")
dijkstra(g, 1)
