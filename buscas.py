def buscaEmLargura(grafo, origem):
    s = str(origem)
    c = dict.fromkeys(grafo.vertices, False)
    d = dict.fromkeys(grafo.vertices, float("inf"))
    a = dict.fromkeys(grafo.vertices, None)

    c[s] = True
    d[s] = 0

    q = [s]

    before = None
    print("0: " + grafo.vertices[s].valor)
    nivel = 1
    string = str(nivel) + ": "
    while len(q) > 0:
        u = q.pop()
        vizinhos = grafo.vizinhos(u)
        if (before != a[u]):
            before = a[u]
            print(string[:len(string)-2])
            nivel += 1
            string = str(nivel) + ": "
        for v in vizinhos:
            if not c[v]:
                c[v] = True
                d[v] = d[u] + 1
                a[v] = u
                q.insert(0, v)
                string += grafo.vertices[v].valor + ", "

    return (d, a)
