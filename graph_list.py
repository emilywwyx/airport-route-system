import random
import math

def generate_airports_coords_and_routes_phase2(
    n,                          # number of airports
    edge_prob = 0.1,            # default param, probability of edge existing (10%)
    coord_range = 1000.0,       # map size, coordinates range for x and y is 0-1000
    directed = True,            # flights are one way
    seed = 42,                  # random seed for reproducibility
    min_factor = 1.1,           # route distance = straight-line distance (euclidean distance) × factor
    max_factor = 2.0,           # multiplier is a value in between min and max
):
    random.seed(seed)

    # generate airport names
    airports = [f"A{i}" for i in range(n)]

    # generate coordinates
    # each airport gets a random 2D (x, y) coordinate
    coords = {}
    for name in airports:
        x = random.uniform(0, coord_range)
        y = random.uniform(0, coord_range)
        coords[name] = (x, y)

    # initialize routs list
    routes = []
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            # decide whether to create an edge, edge_prob is 10% by default
            if random.random() < edge_prob:
                src = airports[i]
                dst = airports[j]
                x1, y1 = coords[src]
                x2, y2 = coords[dst]
                # compute euclidean distance (straight line)
                straight = math.hypot(x1 - x2, y1 - y2)
                factor = random.uniform(min_factor, max_factor)
                # weight (distance) of edge
                w = straight * factor
                routes.append((src, dst, w))
                # add a reverse route for undirected graph
                if not directed:
                    routes.append((dst, src, w))

    return airports, coords, routes

# convert routes into adjacency list
# here we have list instead of matrix (better for sparse graph)
def build_adj_list(airports, routes):
    name_to_idx = {name: i for i, name in enumerate(airports)}
    n = len(airports)
    adj = [[] for _ in range(n)]

    for src, dst, w in routes:
        u = name_to_idx[src]
        v = name_to_idx[dst]
        adj[u].append((v, w))

    return adj, name_to_idx

# convert coords dictionary to list indexed by airport index
def build_coords_idx(airports, coords):
    coords_idx = [None] * len(airports)
    for i, name in enumerate(airports):
        coords_idx[i] = coords[name]
    return coords_idx

# used by A* algorithm to estimate remaining distance
# u = current node index
# target = goal node index
# coords_idx = list of (x, y) coordinates
def heuristic(u, target, coords_idx):

    # get coordinates
    x1, y1 = coords_idx[u]
    x2, y2 = coords_idx[target]

    # euclidean distance
    return math.hypot(x1 - x2, y1 - y2)
