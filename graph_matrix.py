def build_matrix(airports, routes): 
    name_to_idx = {}
    idx_to_name = []

    for i, name in enumerate(airports):
        name_to_idx[name] = i
        idx_to_name.append(name)

    N = len(airports)

    #build the adjacencty matrix
    INF = float("inf")
    #a N * N matrix, and every element initialized to infinity(the weight)
    graph = [[INF]*N for _ in range(N)]

    for i in range(N):
        graph[i][i] = 0 #airport to itself is 0

    for src, des, dist in routes:
        u = name_to_idx[src]
        v = name_to_idx[des]
        graph[u][v] = dist
    return graph