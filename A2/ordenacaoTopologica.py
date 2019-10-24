def ordenacaoTopologica(g):
    c = dict.fromkeys(g.vertices, False)
    t = dict.fromkeys(g.vertices, float('inf'))
    f = dict.fromkeys(g.vertices, float('inf'))
    tempo = 0
    O = []
    for u in g.vertices.keys():
        if (not c[u]):
            dfs_visit_ot(g, u, c, t, f, tempo, O)
    printValues(g, O)


def printValues(g, l):
    string = ""
    for i in l:
        string += (g.getRotulo(i) + ' -> ')
    print(string[:len(string) - 4])


def dfs_visit_ot(g, s, c, t, f, tempo, O):
    c[s] = True
    tempo += 1
    t[s] = tempo
    for u in g.vizinhos(s, "+"):
        if (not c[u]):
            dfs_visit_ot(g, u, c, t, f, tempo, O)
    tempo += 1
    f[s] = tempo
    O.insert(0, s)
