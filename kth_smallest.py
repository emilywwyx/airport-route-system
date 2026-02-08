# priority queue for candidate paths
import heapq
import random
# for visualization
import matplotlib.pyplot as plt

from algorithms_v2 import dijkstra_from_src_list
from graph_list import (
    generate_airports_coords_and_routes_phase2,
    build_adj_list,
    build_coords_idx,
)

INF = float("inf")


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

# path = list of node indices
# adj = adjacency list
# returns total weight sum along the path
def path_cost(path, adj):
    cost = 0.0
    for i in range(len(path) - 1):          # number of edges = len(path) - 1
        u = path[i]
        v = path[i + 1]
        found = False
        for x, w in adj[u]:
            if x == v:
                cost += w
                found = True
                break
        if not found:
            return INF
    return cost


def k_shortest_paths(adj, src, dst, K):
    dist0, prev0 = dijkstra_from_src_list(src, adj)
    if dist0[dst] == INF:
        return []

    p0 = reconstruct_path(src, dst, prev0)
    if p0 is None:
        return []

    A = [p0]  # founded shortest paths
    B = []    # candidate paths (min-heap on total cost)

    for _ in range(1, K):
        last_path = A[-1]  # work on the newly added path
        n = len(last_path)

        for i in range(n - 1):  # the last nodes cannot be spurred
            spur = last_path[i]
            root_path = last_path[: i + 1]  # determined path before spurred node

            # copy the adjacency list
            adj_modified = [list(neigh) for neigh in adj]

            # remove path after the prefix root_path for all already founded paths
            for p in A:
                if len(p) > i and p[: i + 1] == root_path:
                    u = p[i]
                    v = p[i + 1]
                    adj_modified[u] = [(x, w) for (x, w) in adj_modified[u] if x != v]

            dist_spur, prev_spur = dijkstra_from_src_list(spur, adj_modified)
            if dist_spur[dst] == INF:
                continue

            spur_path = reconstruct_path(spur, dst, prev_spur)
            if spur_path is None:
                continue

            total_path = root_path[:-1] + spur_path
            c = path_cost(total_path, adj)
            heapq.heappush(B, (c, total_path))

        if not B:
            break

        cost_k, path_k = heapq.heappop(B)
        A.append(path_k)

    return A


def find_connected_pair(adj, max_trials=300):
    n = len(adj)
    for _ in range(max_trials):
        s = random.randrange(n)
        t = random.randrange(n)
        if s == t:
            continue
        dist, prev = dijkstra_from_src_list(s, adj)
        if dist[t] < INF:
            p = reconstruct_path(s, t, prev)
            if p is not None:
                return s, t
    return None, None


def visualize_k_paths(coords_idx, airports, paths, costs=None, title="K-shortest paths"):
    xs = [coords_idx[i][0] for i in range(len(coords_idx))]
    ys = [coords_idx[i][1] for i in range(len(coords_idx))]

    plt.figure()
    plt.scatter(xs, ys)

    used = set()
    for p in paths:
        used.update(p)

    for i in used:
        x, y = coords_idx[i]
        plt.text(x, y, airports[i], fontsize=8)

    for idx, p in enumerate(paths):
        px = [coords_idx[v][0] for v in p]
        py = [coords_idx[v][1] for v in p]
        if costs is None:
            label = f"rank {idx+1}"
        else:
            label = f"rank {idx+1} (cost={costs[idx]:.2f})"
        plt.plot(px, py, marker="o", label=label)

    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_k_costs(costs, title="K-shortest path costs"):
    ks = list(range(1, len(costs) + 1))
    plt.figure()
    plt.plot(ks, costs, marker="o")
    plt.xlabel("Path rank (k)")
    plt.ylabel("Total distance (cost)")
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    n = 30
    airports, coords, routes = generate_airports_coords_and_routes_phase2(
        n=n,
        edge_prob=0.25,
        coord_range=1000.0,
        directed=True,
        seed=7,
        min_factor=1.1,
        max_factor=2.0,
    )
    adj, name_to_idx = build_adj_list(airports, routes)
    coords_idx = build_coords_idx(airports, coords)

    src, dst = find_connected_pair(adj)
    if src is None:
        print("No connected pair found in this random graph. Try increasing edge_prob.")
    else:
        K = 3
        paths = k_shortest_paths(adj, src, dst, K)

        src_name = airports[src]
        dst_name = airports[dst]

        if not paths:
            print(f"No k-shortest paths found from {src_name} to {dst_name}.")
        else:
            print(f"Top up to {K} shortest paths from {src_name} → {dst_name}:")
            costs = []
            for i, p in enumerate(paths):
                c = path_cost(p, adj)
                costs.append(c)
                named = [airports[idx] for idx in p]
                print(f"{i+1}: Path = {named}, Cost = {c:.2f}")

            visualize_k_paths(
                coords_idx,
                airports,
                paths,
                costs=costs,
                title=f"Yen: K-shortest paths ({src_name} → {dst_name})",
            )
            plot_k_costs(
                costs,
                title=f"Cost vs k ({src_name} → {dst_name})",
            )
