def floydWarshall(grafo):
    D = [w(grafo)]
    l = grafo.qtdVertices()
    vertices = list(map(int, grafo.vertices.keys()))
    for k in range(l):
        D.append([[0 for i in range(l)] for i in range(l)])
        for u in range(l):
            for v in range(l):
                D[k+1][u][v] = min([D[k][u][v], D[k]
                                    [k][v] + D[k][u][k]])
    for i in range(l):
        string = str(i+1) + ":"
        for j in range(l):
            string += str(D[k][i][j]) + (',' if j < l-1 else '')
        print(string)
    return D


def w(g):
    l = g.qtdVertices()
    vertices = list(g.vertices.keys())
    D = [[0 for i in range(l)] for i in range(l)]
    for u in range(l):
        for v in range(l):
            if (u == v):
                D[u][v] = 0
            else:
                D[u][v] = g.getPeso(vertices[u], vertices[v])
    return D
