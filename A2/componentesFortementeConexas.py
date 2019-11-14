from representacao import Grafo


def componentesFortementeConexas(grafo):
    (c, t, a1, f) = dfs(grafo)
    aT = []
    for a in grafo.arcos:
        aT.append((a.v, a.u, a.peso))
    vT = dict.fromkeys(grafo.vertices, None)
    for v in grafo.vertices.keys():
        vT[v] = grafo.vertices[v].invertVertices()
    g = Grafo(None, [vT, aT])
    (ct, tt, art, ft) = dfs_adaptado(g, f)
    output = splitValues(art)
    printLists(output)


def printLists(lists):
    for l in lists:
        if (len(l) > 1):
            print(str(l).replace('[', '').replace(']', '').replace('\'', ''))


def splitValues(a):
    values = []
    for i in a.keys():
        index = findIn(a[i], values)
        if (index >= 0):
            values[index].append(i)
        else:
            values.append([i])
    return values


def findIn(i, lists):
    for l in lists:
        if (i in l):
            return lists.index(l)
    return -1


def dfs(grafo):
    c = dict.fromkeys(grafo.vertices, False)
    t = dict.fromkeys(grafo.vertices, float("inf"))
    f = dict.fromkeys(grafo.vertices, float("inf"))
    a = dict.fromkeys(grafo.vertices, None)
    tempo = 0
    for v in grafo.vertices.keys():
        if not c[v]:
            tempo = dfsVisit(grafo, v, c, t, a, f, tempo)
    return (c, t, a, f)


def dfs_adaptado(grafo, F):
    c = dict.fromkeys(grafo.vertices, False)
    t = dict.fromkeys(grafo.vertices, float("inf"))
    f = dict.fromkeys(grafo.vertices, float("inf"))
    a = dict.fromkeys(grafo.vertices, None)
    tempo = 0
    ordered = sorted(F.keys(), key=lambda x: F[x], reverse=True)
    for v in ordered:
        if not c[v]:
            tempo = dfsVisit(grafo, v, c, t, a, f, tempo)
    return (c, t, a, f)


def dfsVisit(g1, u, c, t, a, f, tempo):
    c[u] = True
    tempo += 1
    t[u] = tempo
    vizinhos = g1.vizinhos(u, "+")
    for v in vizinhos:
        if not c[v]:
            a[v] = u
            tempo = dfsVisit(g1, v, c, t, a, f, tempo)
    tempo += 1
    f[u] = tempo
    return tempo
