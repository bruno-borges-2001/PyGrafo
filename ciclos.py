def cicloEuleriano(grafo):
  c = {}
  for e in grafo.arestas:
    c[str(e)] = False
  
  v = grafo.vertices["1"]

  response = buscarSubcicloEuleriano(grafo, v, c)

  if not response[0]:
    return (False, None)
  else:
    if False in c:
      return (False, None)
    else:
      return (True, response[1])


def buscarSubcicloEuleriano(grafo, v, c):
  ciclo = [v]

  t = v
  while (1):
    found = False
    vizinhos = v.vizinhos
    for key, value in c.items():
      splitted = key.split('-')
      if splitted[0] in vizinhos or splitted[1] in vizinhos:
        found = True
        c[key] = True
        v = splitted[0] if splitted[1] in vizinhos else splitted[1]
        ciclo.append(v)
        break
    if not found:
      return (False, None)
    if v == t:
      break

  for i in ciclo:
    vizinhos = grafo.vizinhos(i)
    