def hopcroftKarp(grafo):
    d = dict.fromkeys(grafo.vertices, float('inf'))
    mate = dict.fromkeys(grafo.vertices, False)

    m = 0
    (c, mate, d) = BFS(grafo, mate, d)
    while c:
        for x in grafo.x.keys():
            if not mate[x]:
                (c2, mate, d) = DFS(grafo, mate, x, d)
                if c2:
                        m += 1
        (c, mate, d) = BFS(grafo, mate, d)
    return (m, mate)


def BFS(grafo, mate, d):
    q = []
    for x in grafo.x.keys():
        if not mate[x]:
            d[x] = 0
            q.append(x)
        else:
            d[x] = float('inf')
    d['null'] = float('inf')
    while len(q) > 0:
        x = q.pop()
        if d[x] < d['null']:
            for y in grafo.vertices[x].getVizinhos():
                if d[mate[str(y)]] == float('inf'):
                    d[mate[str(y)]] = d[x] + 1
                    q.append(mate[str(y)])
    return (d['null'] != float('inf'), mate, d)


def DFS(grafo, mate, x, d):
    if x:
        for y in grafo.vertices[x].getVizinhos():
            if d[mate[str(y)]] == d[x] + 1:
                if DFS(grafo, mate, mate[str(y)], d):
                    mate[str(y)] = x
                    mate[str(x)] = y
                    return (True, mate, d)
        d[x] = float('inf')
        return (False, mate, d)
    return (True, mate, d)
