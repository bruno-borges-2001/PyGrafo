from graph import NonDirectedGraph


def lawler(g):
    x = [0] * ((2 ^ len(g.vertices)) - 1)
    x[0] = 0
    S = potencia(g.vertices.keys())
    for s in S[1:]:
        _s = S.index(s)
        x[_s] = float('inf')
        _g = NonDirectedGraph(createVertices(s), createArestas(s))
        for I in I(_g):
            i = S.index(s - I)
            if i + 1 < x[_s]:
                x[_s] = x[i] + 1
        return x[len(x)-1]


def createVertices(S):
    string = ''
    for i in S:
        string += i + ' "aux"'
    return string


def createArestas(S):
    string = ''
    for u in S:
        for v in S:
            string += u + ' ' + v + ' 1.0\n'
    return string


def I(G):
  # TODO IMPLEMENTAR CONJUNTOS MAXIMAIS
    pass


def potencia(c):
    if len(c) == 0:
        return [[]]
    r = potencia(c[:-1])
    return r + [s + [c[-1]] for s in r]
