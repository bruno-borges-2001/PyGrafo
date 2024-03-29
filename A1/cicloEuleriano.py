def hierholzer(grafo):

    c = {}
    for e in grafo.arestas:
        c[str(e)] = False

    for v in grafo.vertices.keys():
        result = buscarSubcicloEuleriano(grafo, v, c)

        if not result[0]:
            continue
        else:
            if False in c:
                print("0")
                return (False, None)
            else:
                print("1")
                print(str(list(map(lambda x: grafo.vertices[str(x)].valor, result[1]))).replace(
                    '[', '').replace(']', '').replace('\'', ''))
                return (True, result[1])
    print('0')
    return (False, None)


def buscarSubcicloEuleriano(g, v, c):
    ciclo = [v]
    t = v
    while (1):
        found = False
        vizinhos = g.vizinhos(v)
        for u in vizinhos:
            aresta = u + '-' + v if u < v else v + '-' + u
            if aresta in c and c[aresta] == False:
                c[aresta] = True
                v = u
                ciclo.append(v)
                found = True
                break
        if not found:
            return (False, None)
        if v == t:
            break

    for i in ciclo:
        vizinhos = g.vizinhos(i)
        for u in vizinhos:
            aresta = str((i, u)) if i < u else str((u, i))
            if aresta in c and c[aresta] == False:
                result = buscarSubcicloEuleriano(g, i, c)
                if not result[0]:
                    return (False, None)
                map(lambda x: ciclo.insert(
                    ciclo.index(i) + result[1].index(x), x), list(result[1])[1:len(list(result[1]))-1])
    return (True, ciclo)
