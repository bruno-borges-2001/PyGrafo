class Vertice:
    def __init__(self, valor):
        self.valor = valor
        self.grau = 0
        self.vizinhos_out = []
        self.vizinhos_in = []

    def adicionarVizinho(self, v, tag):
        self.incrementarGrau()
        if tag == '+':
            if v not in self.vizinhos_out:
                self.vizinhos_out.append(v)
        elif tag == '-':
            if v not in self.vizinhos_in:
                self.vizinhos_in.append(v)

    def incrementarGrau(self):
        self.grau += 1

    def getVizinhos(self, tag):
        if tag == '+':
            return self.vizinhos_out
        elif tag == '-':
            return self.vizinhos_in
        else:
            return self.vizinhos_in + list(self.vizinhos_out - self.vizinhos_in)


class Aresta:
    def __init__(self, u, v, peso):
        self.u = u
        self.v = v
        self.peso = peso

    def __str__(self):
        return self.u + "-" + self.v

    def __str__(self):
        return str((self.u, self.v))


class Grafo:

    def __init__(self, file=None, values=None):
        self.vertices = {}
        self.arestas = []
        if file is not None:
            self.ler(file)
        if values is not None:
            self.vertices = values[0]
            self.arestas = values[1]

    def adicionarVertice(self, chave, valor):
        self.vertices[chave] = Vertice(valor)

    def adicionarAresta(self, u, v, peso):
        self.arestas.append(Aresta(u, v, peso))
        self.vertices[u].adicionarVizinho(v, '+')
        self.vertices[v].adicionarVizinho(u, '-')

    def qtdVertices(self):
        return len(self.vertices)

    def qtdArestas(self):
        return len(self.arestas)

    def getGrau(self, chave):
        return self.vertices[str(chave)].grau

    def getRotulo(self, chave):
        return self.vertices[str(chave)].valor

    def vizinhos(self, chave, tag):
        return self.vertices[str(chave)].getVizinhos(tag)

    def haAresta(self, u, v):
        aresta = (u, v)
        return next(
            (x for x in self.arestas if x.u == str(aresta[0]) and x.v == str(aresta[1])), None) is not None

    def getPeso(self, u, v):
        try:
            aresta = (u, v)
            value = next(
                (x for x in self.arestas if x.u == str(aresta[0]) and x.v == str(aresta[1])), None)
            return float(value.peso)
        except:
            return float("inf")

    def ler(self, file):
        try:
            f = open(file, "r")
            lines = f.readlines()
            mode = ""
            for line in lines:
                if ("*vertices" in line):
                    mode = "vertices"
                elif ("*edges" in line):
                    mode = "arestas"
                elif ("*arcs" in line):
                    mode = "arcos"
                else:
                    if (mode == "vertices"):
                        values = line.split(' ', 1)
                        self.adicionarVertice(
                            values[0], values[1].replace('"', '').replace('\n', ''))
                    elif (mode == "arestas" or mode == "arcos"):
                        values = line.split(' ')
                        self.adicionarAresta(
                            values[0], values[1], values[2].replace('\n', ''))
        finally:
            f.close()
