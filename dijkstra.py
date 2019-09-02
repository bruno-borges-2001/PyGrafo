def dijkstra(g, origem):
    s = str(origem)
    c = dict.fromkeys(g.vertices, False)
    d = dict.fromkeys(g.vertices, float("inf"))
    a = dict.fromkeys(g.vertices, None)
    d[s] = 0
    for i in range(g.qtdVertices()):
        u = str(argmin(filter(lambda x: c[x[0]] == False, d.items())))
        c[u] = True
        vizinhos = g.vizinhos(u)
        for v in vizinhos:
            if (c[str(v)] == False and d[str(v)] > d[u] + g.getPeso(u, v)):
                d[str(v)] = d[u] + g.getPeso(u, v)
                a[str(v)] = u
    for key in g.vertices.keys():
        string = key
        curr = key
        while (a[curr] != None):
            curr = a[curr]
            string = curr + "," + string
        print(key + ": " + string + "; d = " + str(d[key]))
    return (d, a)


def argmin(d):
    menor = None
    menorKey = None
    for i in d:
        if (menor == None or i[1] < menor):
            menor = i[1]
            menorKey = i[0]
    return menorKey
