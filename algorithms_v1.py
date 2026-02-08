# double ended queue for BFS, efficient (add to end, remove from front in O(1))
# FIFO
from collections import deque
# implements min-heap for Dijkstra to get minimum distance node efficiently
import heapq

INF = float("inf")

# implement BFS traversal
# s = source node airport index, not name!
# graph = the adjacency matrix returned by build_matrix()
def bfs_from_src(s, graph):
    n = len(graph)          # number of rows in matrix = number of airports
    step = [INF] * n        # steps from source to each node, initially INF
    visited = [False] * n   # prevent visiting same node twice
    queue = deque()         # create empty queue for BFS

    visited[s] = True       # mark source as visited
    step[s] = 0             # steps from source to itself is 0 (base case)
    queue.append(s)         # add source to queue

    while queue:
        u = queue.popleft()     # remove and return leftmost element

        # explore all non-visited neighbors of u and incremet step count, add to queue
        for v in range(n):
            if graph[u][v] < INF and not visited[v]:
                visited[v] = True
                step[v] = step[u] + 1
                queue.append(v)
    return step

# implement DFS
# explore as deep as possible before backtracking
def dfs_from_src(s, graph):
    n = len(graph)
    visited = [False] * n
    order = []
    
    # define a nested function
    def dfs(u):
        visited[u] = True
        order.append(u)
        for v in range(n):
            if graph[u][v] < INF and not visited[v]:
                dfs(v)      # explores v and all its children before returning

    # explore dfs from source
    dfs(s)

    # visited = array of booleans indicating which nodes were reachable
    # order = sequence of nodes visited in DFS order
    return visited, order



# implement Dijkstra algorithm
# find shortest path considering actual weights
def dijkstra_from_src(s, graph):
    n = len(graph)
    dist = [INF] * n
    prev = [-1] * n         # store the previous node in the optimal path, -1 means undefined
    pq = []                 # priority queue for min-heap, smallest distance on top. stoered in (distance, node) pairs
    dist[s] = 0             # distance from source to itself is 0

    heapq.heappush(pq, (0, s))      # add tuple to pq

    # greedy choice: always process closest unprocessed node
    # this is correct because all edge weights are non-negative, so once a node has the smallest tentative distance among all unprocessed nodes, no future path can make it shorter.
    while pq:
        d, u = heapq.heappop(pq)    # remove and return smallest distance node, d = distance, u = node
        if d > dist[u]:             # abandon unoptimal entries
            continue

        for v in range(n):
            if d + graph[u][v] < dist[v]:       # found a shorter path to v through u
                dist[v] = d + graph[u][v]       # update total distance to v (optimal)
                prev[v] = u                     # update predecessor of v to u
                heapq.heappush(pq, (dist[v], v))

    # dist = shortest distance to all nodes from source
    # prev = previous node in optimal path
    return dist, prev

# reconstruct the route
# take shortest path tree and extracts specific path
def reconstruct_Dijkstra(start, target, prev):
    path = []                           # will store nodes in path
    current = target                    # start from target, work backwords to source
    while current != -1:                # -1 is the source's predecessor
        path.append(current)
        if current == start:
            break
        current = prev[current]
    path.reverse()
    if not path or path[0] != start:
        return None 
    return path

