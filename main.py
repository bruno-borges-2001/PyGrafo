from grafo import Grafo
from buscas import buscaEmLargura
from ciclos import hierholzer
from dijkstra import dijkstra

g = Grafo("tests/fln_pequena.net")

dijkstra(g, 1)
