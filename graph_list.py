import random
import math

def generate_airports_coords_and_routes_phase2(
    n,
    edge_prob=0.1,
    coord_range=1000.0,
    directed=True,
    seed=42,
    min_factor=1.1,
    max_factor=2.0,
):
    random.seed(seed)

    airports = [f"A{i}" for i in range(n)]

    coords = {}
    for name in airports:
        x = random.uniform(0, coord_range)
        y = random.uniform(0, coord_range)
        coords[name] = (x, y)

    routes = []
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if random.random() < edge_prob:
                src = airports[i]
                dst = airports[j]
                x1, y1 = coords[src]
                x2, y2 = coords[dst]
                straight = math.hypot(x1 - x2, y1 - y2)
                factor = random.uniform(min_factor, max_factor)
                w = straight * factor
                routes.append((src, dst, w))
                if not directed:
                    routes.append((dst, src, w))

    return airports, coords, routes

def build_adj_list(airports, routes):
    name_to_idx = {name: i for i, name in enumerate(airports)}
    n = len(airports)
    adj = [[] for _ in range(n)]

    for src, dst, w in routes:
        u = name_to_idx[src]
        v = name_to_idx[dst]
        adj[u].append((v, w))

    return adj, name_to_idx

def build_coords_idx(airports, coords):
    coords_idx = [None] * len(airports)
    for i, name in enumerate(airports):
        coords_idx[i] = coords[name]
    return coords_idx

def heuristic(u, target, coords_idx):
    x1, y1 = coords_idx[u]
    x2, y2 = coords_idx[target]
    return math.hypot(x1 - x2, y1 - y2)
