from representacao import Grafo


def componentesFortementeConexas(grafo):
    (c, t, a1, f) = dfs(grafo)
    aT = []
    for a in grafo.arestas:
        aT.append((a.v, a.u, a.peso))
    g = Grafo(None, [grafo.vertices, aT])
    (ct, tt, art, ft) = dfs_adaptado(g)
    output = splitValues(art)
    printLists(output)


def printLists(lists):
    for l in lists:
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
            dfsVisit(grafo, v, c, t, a, f, tempo)
    return (c, t, a, f)


def dfs_adaptado(grafo):
    c = dict.fromkeys(grafo.vertices, False)
    t = dict.fromkeys(grafo.vertices, float("inf"))
    f = dict.fromkeys(grafo.vertices, float("inf"))
    a = dict.fromkeys(grafo.vertices, None)
    tempo = 0
    ordered = sorted(grafo.vertices, key=lambda x: f[x])
    for v in ordered:
        if not c[v]:
            dfsVisit(grafo, v, c, t, a, f, tempo)
    return (c, t, a, f)


def dfsVisit(grafo, v, c, t, a, f, tempo):
    c[v] = True
    tempo = tempo + 1
    t[v] = tempo
    vizinhos = grafo.vizinhos(v, "+")
    for u in vizinhos:
        if not c[u]:
            a[u] = v
            dfsVisit(grafo, u, c, t, a, f, tempo)
    tempo = tempo + 1
    f[v] = tempo
