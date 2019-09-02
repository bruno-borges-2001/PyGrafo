from grafo import Grafo
from buscas import buscaEmLargura
from ciclos import hierholzer

g = Grafo("tests/celegansneural.net")

print(hierholzer(g))
