def componentesFortementeConexas(grafo):
    (c, t, a1, f) = dfs(grafo)
    aT = []
    for (u,v,w) in grafo.arestas:
        aT.add((v,u,w))





def dfs(grafo):
    c = dict.fromkeys(grafo.vertices, False)
    t = dict.fromkeys(grafo.vertices, float("inf"))
    f = dict.fromkeys(grafo.vertices, float("inf"))
    a = dict.fromkeys(grafo.vertices, None)
    tempo = 0
    for v in grafo.vertices.keys():
        if not c[v]:
            dfsVisit(grafo, v, c, t, a, f, tempo)
    return (c, t, a, f)


def dfsVisit(grafo, v, c, t, a, f, tempo):
    c[v] = True
    tempo = tempo + 1
    t[v] = tempo
    vizinhos = grafo.vizinhos(v)
    for u in vizinhos:
        if not c[u]:
            a[u] = v
            dfsVisit(grafo, u, c, t, a, f, tempo)
    tempo = tempo + 1
    f[v] = tempo