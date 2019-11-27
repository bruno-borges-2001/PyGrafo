from graph import NonDirectedGraph, DirectedGraph


def readFile(file):
    try:
        f = open(file, 'r')
        lines = f.readlines()
        mode = 'missing'
        vertices = []
        arestas = []
        arcos = []
        for l in lines:
            if ('*vertices' in l):
                mode = 'vertices'
            elif ('*arcs' in l):
                mode = 'arcs'
            elif ('*edges' in l):
                mode = 'edges'
            else:
                if (mode == 'vertices'):
                    vertices.append(l.replace('\n', ''))
                elif (mode == 'arcs'):
                    arcos.append(l.replace('\n', ''))
                elif (mode == 'edges'):
                    arestas.append(l.replace('\n', ''))
        if (mode == 'arcs'):
            return DirectedGraph(vertices, arcos)
        elif (mode == 'edges'):
            return NonDirectedGraph(vertices, arestas)
    finally:
        f.close()
