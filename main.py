from grafo import Grafo
from buscas import buscaEmLargura
from ciclos import cicloEuleriano

g = Grafo("./tests/agm_tiny.net")

cicloEuleriano(g)
