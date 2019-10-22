def kruskal(g):
    A = []
    S = {}
    for v in g.vertices.keys():
        S[v] = [g.vertices[v]]
    E = sorted(g.arestas, key=lambda x: x.peso)
    for a in E:
        if S[str(a.u)] != S[str(a.v)]:
            A.append((a.u, a.v))
            x = S[str(a.u)] + S[str(a.v)]
            for w in x:
                S[str(w)] = x
    peso = 0
    for i in A:
        peso += g.getPeso(i[0], i[1])
    print(peso)
    print(str(A).replace('\', \'', '-').replace('[', '').replace(']', '').replace(
        '\'', '').replace('(', '').replace(')', ''))
