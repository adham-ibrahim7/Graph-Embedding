from typing import List, Any


class Graph:

    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = [list() for _ in range(V)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)
        self.E += 1

    def add_directed_edge(self, u, v):
        self.adj[u].append(v)
        self.E += 1

    def __str__(self):
        str_rep = ""
        for u in range(self.V):
            str_rep += str(u) + ": " + str(self.adj[u])
            if u < self.V-1:
                str_rep += "\n"
        return str_rep
