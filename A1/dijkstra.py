def dijkstra(g, origem):
    s = str(origem)
    c = dict.fromkeys(g.vertices, False)
    d = dict.fromkeys(g.vertices, float("inf"))
    a = dict.fromkeys(g.vertices, None)
    d[s] = 0
    for _ in range(len(g.vertices)):
        u = str(argmin(filter(lambda x: c[x[0]] == False, d.items())))
        c[u] = True
        vizinhos = g.vizinhos(u)
        for v in vizinhos:
            if (c[v] == False and d[v] > d[u] + g.findAresta(u, v).peso):
                d[str(v)] = d[u] + g.findAresta(u, v).peso
                a[str(v)] = u
    for key in sorted(g.vertices.keys(), key=int):
        string = g.vertices[str(key)].valor
        curr = key
        while (a[curr] != None):
            curr = a[curr]
            string = g.vertices[str(curr)].valor + "," + string
        print(str(key) + ": " + string + "; d = " + str(d[key]))
    return (d, a)


def argmin(d):
    menor = None
    menorKey = None
    for i in d:
        if (menor == None or i[1] < menor):
            menor = i[1]
            menorKey = i[0]
    return menorKey
