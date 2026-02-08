from collections import deque
import heapq
import random
from graph_list import (
    build_adj_list,
    build_coords_idx,
    heuristic,
)

INF = float("inf")

# bfs adjacency list
# similar to what we did in v1, just with list here instead of matrix
def bfs_from_src_list(s, adj):
    n = len(adj)
    step = [INF] * n 
    visited = [False] * n 
    step[s] = 0
    q = deque()
    visited[s] = True
    q.append(s)

    # key difference here is that for phase 1 BFS checks all n nodes
    # in phase 2 with adjacency list only check actual neighbors out of n
    while q:
        u = q.popleft()
        for v, w in adj[u]:                 # adj[u] = list of (neighbor, weight) tuples
            if not visited[v]:
                step[v] = step[u] + 1
                q.append(v)
                visited[v] = True
    return step

# dfs adjacency list
def dfs_from_src_list(s, adj):
    n = len(adj)
    visited = [False] * n 
    order = []
    def dfs(u):
        visited[u] = True
        order.append(u)
        for v, w in adj[u]:                 # again only check actual neighbors
            if not visited[v]:
                dfs(v)
    dfs(s)
    return visited, order

def dijkstra_from_src_list(s, adj):
    n = len(adj)
    dist = [INF] * n 
    prev = [-1] * n 
    dist[s] = 0
    pq = []
    heapq.heappush(pq, (0, s))
    while pq:
        d, u = heapq.heappop(pq)
        # stale state check
        if d > dist[u]:
            continue
        for v, w in adj[u]:                 # O(degree(u)) per node
            new_d = dist[u] + w
            if new_d < dist[v]:
                dist[v] = new_d
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))
    return dist, prev

# src = source airport index
# des = destination airport index
# adj = adjacency list
# coords_idx = list of (x, y) coordinates indexed by airport index
def astar(src, des, adj, coords_idx):
    n = len(adj)
    g = [INF] * n               # g = actual cost from source to each node
    prev = [-1] * n 
    g[src] = 0.0                # zero cost to reach source
    pq = []
    h0 = heuristic(src, des, coords_idx)        # estimated cost from source to destination
    heapq.heappush(pq, (h0, 0.0, src))

    # difference from Dijkstra
    # Dijkstra: explore all reachable nodes
    # A*: stops as soon as destination found
    # Picks node that seems closest to completing path to destination
    while pq:
        f, cur_g, u = heapq.heappop(pq)
        if u == des:
            break
        if cur_g > g[u]:
            continue
        
        for v, w in adj[u]:
            new_g = g[u] + w 
            if new_g <g[v]:
                g[v] = new_g
                prev[v] = u 
                hv = heuristic(v, des, coords_idx)
                f_v = new_g + hv
                #use the sum of Euclidean length from current node to destination and flight distance from scource to current as the sorting key in priority queue
                heapq.heappush(pq, (f_v, new_g, v))

    # g = final distances
    # prev = predecessor
    return g, prev

# build path from prev array
def reconstruct_path(start, target, prev):
    path = []
    cur = target
    while cur != -1:
        path.append(cur)
        if cur == start:
            break
        cur = prev[cur]
    path.reverse()
    if not path or path[0] != start:
        return None
    return path

# helper functions to run all pairs for testing
# runs BFS, DFS, Dijkstra, A* n times (once from each node)
def bfs_all_sources(adj):
    n = len(adj)
    for s in range(n):
        bfs_from_src_list(s, adj)

def dfs_all_sources(adj):
    n = len(adj)
    for s in range(n):
        dfs_from_src_list(s, adj)

def dijkstra_all_sources(adj):
    n = len(adj)
    for s in range(n):
        dijkstra_from_src_list(s, adj)

def astar_random_pairs(adj, coords_idx, num_pairs=50, seed=0):
    n = len(adj)
    rnd = random.Random(seed)
    for _ in range(num_pairs):
        s = rnd.randrange(n)
        t = rnd.randrange(n)
        while t == s:
            t = rnd.randrange(n)
        astar(s, t, adj, coords_idx)
