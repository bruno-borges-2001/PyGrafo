from A1.buscas import buscaEmLargura
from A1.cicloEuleriano import hierholzer
from A1.dijkstra import dijkstra
from A1.floydWarshall import floydWarshall

from A2.componentesFortementeConexas import componentesFortementeConexas
from A2.ordenacaoTopologica import ordenacaoTopologica


class Vertice:
    def __init__(self, i, label):
        self.id = i
        self.valor = label
        self.grau = 0
        self.vizinhos_out = []
        self.vizinhos_in = []

    def adicionarVizinho(self, v, tag='+'):
        self.incrementarGrau()
        if tag == '+':
            if v not in self.vizinhos_out:
                self.vizinhos_out.append(v)
        elif tag == '-':
            if v not in self.vizinhos_in:
                self.vizinhos_in.append(v)

    def incrementarGrau(self):
        self.grau += 1

    def getVizinhos(self, tag=None):
        if tag == '+':
            return self.vizinhos_out
        elif tag == '-':
            return self.vizinhos_in
        else:
            return list(set(self.vizinhos_in + self.vizinhos_out))

    def invertVertices(self):
        aux = self.vizinhos_in
        self.vizinhos_in = self.vizinhos_out
        self.vizinhos_out = aux
        return self

    def __str__(self, vizinhos=False):
        if (vizinhos):
            return self.getVizinhos()
        else:
            return str(self.id) + " - " + str(self.valor)


class Aresta:
    def __init__(self, u, v, peso):
        self.u = u
        self.v = v
        self.peso = peso

    def __str__(self):
        return self.u + "-" + self.v

    def __eq__(self, other):
        return (self.u == other.u and self.v == other.v) or (self.u == other.v and self.v == other.u)


class Arco(Aresta):
    def __init__(self, u, v, peso):
        super().__init__(u, v, peso)

    def getInvertedArc(self):
        return Arco(self.v, self.u, self.peso)

    def __eq__(self, other):
        return (self.u == other.u and self.v == other.v)


class Graph:

    def __init__(self, vertices, func=None):
        self.vertices = self.readVertices(vertices)
        self.c = func

    def vizinhos(self, u, tag=None):
        return self.vertices[str(u)].getVizinhos(tag)

    def readVertices(self, vertices):
        v = {}
        for line in vertices:
            values = line.split(' ')
            i = values[0]
            label = values[1].replace('"', '')
            v[str(i)] = Vertice(i, label)
        return v


class NonDirectedGraph(Graph):

    def __init__(self, vertices, arestas, func=None):
        super().__init__(vertices, func)
        self.arestas = self.readArestas(arestas)

    def findAresta(self, u, v):
        aux = Aresta(u, v, 0)
        return next((x for x in self.arestas if x == aux), None)

    def haAresta(self, u, v):
        aux = self.findAresta(u, v)
        return aux is not None

    def BFS(self, origin):
        return buscaEmLargura(self, origin)

    def cicloEuleriano(self):
        return hierholzer(self)

    def HamiltonianDijkstra(self, origin):
        return dijkstra(self, origin)

    def HamiltonianFloydWarshall(self):
        return floydWarshall(self)

    def readArestas(self, arestas):
        a = []
        for line in arestas:
            values = line.split(' ')
            u = values[0]
            v = values[1]
            peso = self.c(u, v) if self.c is not None else values[2]
            a.append(Aresta(u, v, float(peso)))
            self.vertices[str(u)].adicionarVizinho(v)
            self.vertices[str(v)].adicionarVizinho(u)
        return a

    def __str__(self):
        string = "Vertices:\n"
        string += str(list(map(str, self.vertices.values())))
        string += "\nArestas:\n"
        string += str(list(map(str, self.arestas)))
        return string.replace('[', '').replace(']', '').replace(':\n', ':\n ').replace('\',', ',\n').replace('\'', '')


class DirectedGraph(Graph):

    def __init__(self, vertices, arcos, func=None):
        super().__init__(vertices, func)
        self.arcos = self.readArcs(arcos)

    def findArco(self, u, v):
        aux = Arco(u, v, 0)
        return next((x for x in self.arcos if x == aux), None)

    def haArco(self, u, v):
        aux = self.findArco(u, v)
        return aux is not None

    def CFC(self):
        return componentesFortementeConexas(self)

    def TopologicalSort(self):
        return ordenacaoTopologica(self)

    def readArcs(self, arcos):
        a = []
        for line in arcos:
            values = line.split(' ')
            u = values[0]
            v = values[1]
            peso = values[2]
            a.append(Arco(u, v, float(peso)))
            self.vertices[str(u)].adicionarVizinho(v, '+')
            self.vertices[str(v)].adicionarVizinho(u, '-')
        return a
