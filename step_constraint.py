import heapq
INF = float("inf")

def route_min_stops_then_cost(adj, src, dst, max_stops):
    """
    Lexicographic optimization:
      1) minimize number of stops (equivalently edges)
      2) among same edges, minimize total cost
    Constraint:
      edges <= max_edges = max_stops + 1

    Returns:
      (best_steps, best_cost, path) or (None, INF, None) if impossible
    """
    n = len(adj)
    max_edges = max_stops + 1

    dist = [[INF] * n for _ in range(max_edges + 1)]
    parent = [[-1] * n for _ in range(max_edges + 1)]

    dist[0][src] = 0.0
    pq = [(0, 0.0, src)]  # (steps, cost, node)

    while pq:
        steps, cost_u, u = heapq.heappop(pq)
        if cost_u != dist[steps][u]:
            continue

        if u == dst:
            path = reconstruct_constrained_path(parent, src, dst, steps)
            return steps, cost_u, path

        if steps == max_edges:
            continue

        ns = steps + 1
        for v, w in adj[u]:
            nd = cost_u + w
            if nd < dist[ns][v]:
                dist[ns][v] = nd
                parent[ns][v] = u
                heapq.heappush(pq, (ns, nd, v))

    return None, INF, None


def reconstruct_constrained_path(parent, src, dst, steps):
    path = []
    cur = dst
    s = steps
    while True:
        path.append(cur)
        if cur == src and s == 0:
            break
        prev = parent[s][cur]
        if prev == -1:
            return None
        cur = prev
        s -= 1
    path.reverse()
    return path
