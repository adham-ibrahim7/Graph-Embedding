class Graph:

    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = [list() for _ in range(V)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)
        self.E += 1


g = Graph(10)

g.add_edge(0, 1)
