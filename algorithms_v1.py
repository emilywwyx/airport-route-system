from collections import deque
import heapq


INF = float("inf")
#implement BFS traversal

def bfs_from_src(s, graph):
    n = len(graph)
    dist = [INF] * n
    visited = [False] * n
    queue = deque()

    visited[s] = True
    dist[s] = 0
    queue.append(s)

    while queue:
        u = queue.popleft()
        for v in range(n):
            if graph[u][v] < INF and visited[v]==False:
                visited[v] = True
                dist[v] = dist[u] + 1
                queue.append(v)

    return dist

#implement DFS
def dfs_from_src(s, graph):
    n = len(graph)
    dist = [INF] * n
    visited = [False] * n
    order = []
    
    def dfs(u):
        visited[u] = True
        order.append(u)
        for v in range(n):
            if graph[u][v] < INF and not visited[v]:
                dfs(v)
    dfs(s)
    return visited, order



#implement Dijkstra algorithm
def dijkstra_from_src(s, graph):
    n = len(graph)
    dist = [INF] * n
    prev = [-1] * n
    pq = []
    dist[s] = 0

    heapq.heappush(pq, (0, s))

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue

        for v in range(n):
            if d + graph[u][v] < dist[v]:
                dist[v] = d + graph[u][v]
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))

    return dist, prev

#reconstruct the route
def reconstruct_Dijkstra(start, target, prev):
    start = name_to_idx(start)
    target = name_to_idx(target)
    path = []
    current = target
    while current != -1:
        path.append(current)
        if current == start:
            break
        current = prev[current]
    path.reverse()
    if not path or path[0] != start:
        return None 
    return path

