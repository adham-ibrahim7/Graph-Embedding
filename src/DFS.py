from graph import Graph


def dfs(G: Graph) -> tuple[dict[int], dict[int], dict[int], Graph]:
    """
    Perform DFS search of G.
    Assign a unique DFS index to each node, starting with 1, in the order the nodes are first visited.
    Assign a parent to each node.
    Assign the first lowpoint of each node, the smallest dfi index of the subtree of nodes reachable by tree edges from
    a given node, followed by at most one back edge.
    Direct every edge in G in a new digraph D. In D, every edge u->v with dfi[u] < dfi[v] is a tree edge, the
    rest are back edges.

    :param G
    :return: dfi: dict, parent: dict, first_lowpoint: dict, D: Graph
    """

    parent = {}
    dfi = {}
    first_lowpoint = {}

    D = Graph(G.V)
    # TODO: avoid auxillary graph?
    G_copy = Graph(G.V)

    current_label = 1

    for start_vertex in range(0, G.V):
        if start_vertex in dfi:
            continue

        u = start_vertex
        dfi[u] = current_label
        first_lowpoint[u] = dfi[u]
        current_label += 1

        finished = False

        while not finished:
            if not G.adj[u]:
                if u == start_vertex:
                    # returned to root
                    finished = True
                else:
                    # back-track to parent; check lowpoint
                    if first_lowpoint[parent[u]] > first_lowpoint[u]:
                        first_lowpoint[parent[u]] = first_lowpoint[u]
                    u = parent[u]
            else:
                v = G.adj[u].pop(0)
                G.adj[v].remove(u)
                G_copy.add_edge(u, v)

                D.add_directed_edge(u, v)

                if v not in dfi:
                    # tree edge, undiscovered v
                    parent[v] = u
                    u = v
                    dfi[u] = current_label
                    first_lowpoint[u] = dfi[u]
                    current_label += 1
                elif dfi[u] > dfi[v] and first_lowpoint[u] > dfi[v]:
                    # back edge, update lowpoint
                    first_lowpoint[u] = dfi[v]

    G.adj = G_copy.adj

    return dfi, parent, first_lowpoint, D
