from DFS import dfs
from graph import Graph

G = Graph(12)

G.add_edge(0, 4)
G.add_edge(0, 5)
G.add_edge(4, 5)
G.add_edge(2, 4)
G.add_edge(2, 11)
G.add_edge(2, 6)
G.add_edge(4, 9)
G.add_edge(4, 7)
G.add_edge(1, 7)
G.add_edge(1, 10)
G.add_edge(7, 10)
G.add_edge(3, 7)
G.add_edge(3, 9)
G.add_edge(8, 9)
G.add_edge(6, 7)
G.add_edge(4, 6)
G.add_edge(6, 11)

dfi, parent, first_lowpoint, D = dfs(G)

print("parent:", parent)
print("dfs index:", dfi)
print("first lowpoint: ", first_lowpoint)
print(f"underlying digraph, D:\n{D}")
