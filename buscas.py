def buscaEmLargura(grafo, origem):
    s = str(origem)
    c = dict.fromkeys(grafo.vertices, False)
    d = dict.fromkeys(grafo.vertices, float("inf"))
    a = dict.fromkeys(grafo.vertices, None)

    c[s] = True
    d[s] = 0

    q = [s]

    nivel = 0
    while len(q) > 0:
        u = q.pop()
        vizinhos = grafo.vizinhos(u)
        print(str(nivel) + ': ' +
              str(list(map(lambda x: grafo.vertices[str(x)].valor, vizinhos))).replace('[', '').replace(']', '').replace('\'', ''))
        nivel += 1
        for v in vizinhos:
            if not c[v]:
                c[v] = True
                d[v] = d[u] + 1
                a[v] = u
                q.insert(0, v)

    return (d, a)
