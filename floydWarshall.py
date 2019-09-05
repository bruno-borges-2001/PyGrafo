def floydWarshall(grafo):
  D = [w(grafo)]
  l = grafo.qtdVertices()
  vertices = list(map(int, grafo.vertices.keys()))
  print(vertices)
  for k in vertices:
    D.append([[0]*l]*l)
    for u in vertices:
      for v in vertices:
        minimo = min([D[k-1][u-1][v-1], D[k-1][k-1][v-1], D[k-1][u-1][k-1]])
        D[k][u-1][v-1] = minimo
  for i in range(l):
    string = str(i+1) + ":"
    for j in range(l):
      string += str(D[k-1][i][j]) + (',' if j < l-1 else '')
    print(string)
  return D


def w(g):
  l = g.qtdVertices()
  D = [[0] * l] * l
  for u in range(l):
      for v in range(l):
        if (u == v):
          D[u][v] = 0
        else:
          D[u][v] = g.getPeso(u+1, v+1)
  return D
