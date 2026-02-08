import heapq

def astar(src, dst, adj, coords_idx):
    """
    src, dst: int (index of airports)
    adj: adjacency list, adj[u] = [(v, weight), ...]
    coords_idx: list of (x, y) for each index
    return dist, prev
    """
    n = len(adj)
    INF = float("inf")

    g = [INF] * n  
    prev = [-1] * n

    g[src] = 0.0
    # pq store (f, g, node)
    pq = []
    h0 = heuristic(src, dst, coords_idx)
    heapq.heappush(pq, (h0, 0.0, src))

    while pq:
        f, cur_g, u = heapq.heappop(pq)

        if u == dst:
            break

        if cur_g > g[u]:
            continue

        # 遍历邻居
        for v, w in adj[u]:
            new_g = g[u] + w
            if new_g < g[v]:
                g[v] = new_g
                prev[v] = u
                h_v = heuristic(v, dst, coords_idx)
                f_v = new_g + h_v
                heapq.heappush(pq, (f_v, new_g, v))

    return g, prev
