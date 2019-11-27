def floydWarshall(grafo):
    D = [w(grafo)]
    l = len(grafo.vertices)
    for k in range(l):
        D.append([[0 for i in range(l)] for i in range(l)])
        for u in range(l):
            for v in range(l):
                D[k+1][u][v] = min([D[k][u][v], D[k]
                                    [k][v] + D[k][u][k]])
    for i in range(l):
        string = str(i+1) + ":"
        for j in range(l):
            string += str(D[k][i][j]) + (', ' if j < l-1 else '')
        print(string)
    return D


def w(g):
    l = len(g.vertices)
    vertices = list(g.vertices.keys())
    D = [[0 for i in range(l)] for i in range(l)]
    for u in range(l):
        for v in range(l):
            if (u == v):
                D[u][v] = 0
            else:
                a = g.findAresta(vertices[u], vertices[v])
                D[u][v] = a.peso if a is not None else float('inf')
    return D
