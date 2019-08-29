from grafo import Grafo
from buscas import buscaEmLargura

g = Grafo("agm_tiny.net")

print(buscaEmLargura(g, 1))
