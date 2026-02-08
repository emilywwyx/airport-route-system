from time import perf_counter
import random
import matplotlib.pyplot as plt

# Phase 1: matrix-based algorithms
from algorithms_v1 import (
    bfs_from_src,
    dfs_from_src,
    dijkstra_from_src,
)
from graph_matrix import build_matrix

# Phase 2: list-based + A*
from graph_list import (
    generate_airports_coords_and_routes_phase2,
    build_adj_list,
    build_coords_idx,
)
from algorithms_v2 import (
    bfs_all_sources,
    dfs_all_sources,
    dijkstra_all_sources,
    astar_random_pairs,
)

INF = float("inf")

# runs functions multiple times, reports best/average time
def time_algorithm(func, *args, repeat=5):
    times = []
    for _ in range(repeat):
        t0 = perf_counter()
        func(*args)
        t1 = perf_counter()
        times.append(t1 - t0)
    best = min(times)
    avg = sum(times) / len(times)
    return best, avg


# ---------------- Phase 1: random airports + routes + matrix ---------------- #

def generate_random_airports_and_routes(
    n,
    edge_prob=0.1,
    w_min=50,
    w_max=500,
    directed=True,
    seed=42,
):
    random.seed(seed)
    airports = [f"A{i}" for i in range(n)]
    routes = []
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if random.random() < edge_prob:
                w = random.randint(w_min, w_max)
                src = airports[i]
                dst = airports[j]
                routes.append((src, dst, w))
                if not directed:
                    routes.append((dst, src, w))
    return airports, routes


def bfs_all_sources_matrix(graph):
    n = len(graph)
    for s in range(n):
        bfs_from_src(s, graph)


def dfs_all_sources_matrix(graph):
    n = len(graph)
    for s in range(n):
        dfs_from_src(s, graph)


def dijkstra_all_sources_matrix(graph):
    n = len(graph)
    for s in range(n):
        dijkstra_from_src(s, graph)


def run_performance_phase1():
    N_SMALL = 24
    N_MEDIUM = 200
    N_LARGE = 500

    airports_s, routes_s = generate_random_airports_and_routes(
        N_SMALL, edge_prob=0.45, seed=1
    )
    airports_m, routes_m = generate_random_airports_and_routes(
        N_MEDIUM, edge_prob=0.075, seed=2
    )
    airports_l, routes_l = generate_random_airports_and_routes(
        N_LARGE, edge_prob=0.06, seed=3
    )

    matrix_small = build_matrix(airports_s, routes_s)
    matrix_medium = build_matrix(airports_m, routes_m)
    matrix_large = build_matrix(airports_l, routes_l)

    graphs = [
        ("small", matrix_small),
        ("medium", matrix_medium),
        ("large", matrix_large),
    ]

    results = []
    for label, g in graphs:
        n = len(g)
        bfs_best, _ = time_algorithm(bfs_all_sources_matrix, g, repeat=5)
        dfs_best, _ = time_algorithm(dfs_all_sources_matrix, g, repeat=5)
        dijk_best, _ = time_algorithm(dijkstra_all_sources_matrix, g, repeat=5)
        results.append(
            {
                "name": label,
                "n": n,
                "bfs": bfs_best,
                "dfs": dfs_best,
                "dijk": dijk_best,
            }
        )
    return results


# ---------------- Phase 2: coords + adj list + A* ---------------- #

def build_phase2_dataset(n, edge_prob, seed):
    airports, coords, routes = generate_airports_coords_and_routes_phase2(
        n=n,
        edge_prob=edge_prob,
        coord_range=1000.0,
        directed=True,
        seed=seed,
        min_factor=1.1,
        max_factor=2.0,
    )
    adj, name_to_idx = build_adj_list(airports, routes)
    coords_idx = build_coords_idx(airports, coords)
    return airports, coords, routes, adj, coords_idx


def run_performance_phase2():
    N_SMALL = 24
    N_MEDIUM = 200
    N_LARGE = 500

    datasets = [
        ("small", N_SMALL, 0.40, 1),
        ("medium", N_MEDIUM, 0.075, 2),
        ("large", N_LARGE, 0.06, 3),
    ]

    results = []

    for label, n, edge_prob, seed in datasets:
        airports, coords, routes, adj, coords_idx = build_phase2_dataset(
            n, edge_prob, seed
        )

        bfs_best, _ = time_algorithm(bfs_all_sources, adj, repeat=3)
        dfs_best, _ = time_algorithm(dfs_all_sources, adj, repeat=3)
        dijk_best, _ = time_algorithm(dijkstra_all_sources, adj, repeat=3)

        num_pairs = 50 if n >= 50 else n * 2
        astar_best, _ = time_algorithm(
            astar_random_pairs, adj, coords_idx, num_pairs, 0, repeat=3
        )

        m = sum(len(nei) for nei in adj)

        results.append(
            {
                "name": label,
                "n": len(airports),
                "m": m,
                "bfs": bfs_best,
                "dfs": dfs_best,
                "dijk": dijk_best,
                "astar": astar_best,
            }
        )

    return results


# ---------------- Plot: Phase1 only, Phase2 only, comparison ---------------- #

def plot_phase(results, title, show_astar=False):
    results_sorted = sorted(results, key=lambda r: r["n"])
    Ns = [r["n"] for r in results_sorted]
    bfs = [r["bfs"] * 1000 for r in results_sorted]
    dfs = [r["dfs"] * 1000 for r in results_sorted]
    dijk = [r["dijk"] * 1000 for r in results_sorted]

    plt.figure()
    plt.plot(Ns, bfs, marker="o", label="BFS")
    plt.plot(Ns, dfs, marker="s", label="DFS")
    plt.plot(Ns, dijk, marker="^", label="Dijkstra")

    if show_astar and all("astar" in r for r in results_sorted):
        astar = [r["astar"] * 1000 for r in results_sorted]
        plt.plot(Ns, astar, marker="x", label="A*")

    plt.xlabel("Number of vertices N")
    plt.ylabel("Runtime (ms)")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()


def plot_comparison_all(phase1_results, phase2_results):
    p1 = {r["name"]: r for r in phase1_results}
    p2 = {r["name"]: r for r in phase2_results}
    labels = ["small", "medium", "large"]

    Ns = [p1[l]["n"] for l in labels]

    # one color for Phase 1, one color for Phase 2
    phase1_color = "black"
    phase2_color = "0.5"  # gray

    algos = [
        ("bfs", "BFS", "o", "-"),
        ("dfs", "DFS", "s", "--"),
        ("dijk", "Dijkstra", "^", "-."),
    ]

    plt.figure()

    for key, name, marker, ls in algos:
        y1 = [p1[l][key] * 1000 for l in labels]
        y2 = [p2[l][key] * 1000 for l in labels]

        plt.plot(
            Ns, y1,
            marker=marker,
            linestyle=ls,
            color=phase1_color,
            label=f"Phase 1 {name}",
        )

        plt.plot(
            Ns, y2,
            marker=marker,
            linestyle=ls,
            color=phase2_color,
            label=f"Phase 2 {name}",
        )

    plt.xlabel("Number of vertices N")
    plt.ylabel("Runtime (ms)")
    plt.title("Phase 1 vs Phase 2 (BFS / DFS / Dijkstra)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()


if __name__ == "__main__":
    phase1_results = run_performance_phase1()
    phase2_results = run_performance_phase2()

    plot_phase(phase1_results, "Phase 1: adjacency-matrix implementation")
    plot_phase(phase2_results, "Phase 2: adjacency-list + A* implementation", show_astar=True)
    plot_comparison_all(phase1_results, phase2_results)

    plt.show()
