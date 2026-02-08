"""
Airport Route System - Main Interactive Application
"""

import sys

# phase 1 implementation
from graph_matrix import build_matrix
from algorithms_v1 import (
    bfs_from_src,
    dfs_from_src,
    dijkstra_from_src,
    reconstruct_Dijkstra
)

# phase 2 implementation
from graph_list import (
    build_adj_list,
    build_coords_idx,
)
from algorithms_v2 import (
    bfs_from_src_list,
    dfs_from_src_list,
    dijkstra_from_src_list,
    astar,
    reconstruct_path
)

INF = float("inf")

def load_real_airport_data():
    """
    Load real-world airport data for phase 2.
    Returns: (airports, routes, coords)
    """
    airports = [
        "ATL", "AUS", "BOS", "BWI", "DCA", "DEN", "DFW", "DTW",
        "EWR", "IAD", "IAH", "JFK", "LAS", "LAX", "MDW", "MIA",
        "MSP", "PDX", "PHL", "RDU", "SAN", "SEA", "SFO", "SLC"
    ]
    
    # real approximate coordinates (longitude, latitude)
    coords = {
        "ATL": (-84.39, 33.75), "AUS": (-97.74, 30.27),
        "BOS": (-71.01, 42.37), "BWI": (-76.64, 39.29),
        "DCA": (-77.04, 38.91), "DEN": (-104.99, 39.74),
        "DFW": (-96.80, 32.78), "DTW": (-83.05, 42.33),
        "EWR": (-74.17, 40.74), "IAD": (-77.46, 38.88),
        "IAH": (-95.37, 29.76), "JFK": (-73.78, 40.64),
        "LAS": (-115.14, 36.17), "LAX": (-118.24, 34.05),
        "MDW": (-87.63, 41.88), "MIA": (-80.19, 25.76),
        "MSP": (-93.27, 44.98), "PDX": (-122.68, 45.51),
        "PHL": (-75.17, 39.95), "RDU": (-78.79, 35.78),
        "SAN": (-117.16, 32.72), "SEA": (-122.33, 47.61),
        "SFO": (-122.42, 37.77), "SLC": (-111.89, 40.76)
    }
    
    # sample routes with realistic distances (bidirectional)
    # format: (src, dst, distance_miles)
    routes_one_way = [
        # east Coast
        ("BOS", "JFK", 187), ("BOS", "PHL", 280), ("BOS", "DCA", 399),
        ("JFK", "PHL", 94), ("JFK", "DCA", 213), ("JFK", "BWI", 169),
        ("EWR", "JFK", 10), ("EWR", "PHL", 80),
        
        # south
        ("ATL", "MIA", 595), ("ATL", "RDU", 356), ("ATL", "IAH", 689),
        ("MIA", "IAH", 964),
        
        # midwest
        ("DTW", "MDW", 235), ("DTW", "MSP", 528), ("MDW", "MSP", 334),
        
        # west
        ("LAX", "SFO", 347), ("LAX", "SAN", 109), ("LAX", "LAS", 236),
        ("SFO", "SEA", 679), ("SFO", "PDX", 550), ("SEA", "PDX", 129),
        ("DEN", "SLC", 391), ("DEN", "LAS", 628),
        
        # cross-country
        ("JFK", "LAX", 2475), ("JFK", "SFO", 2586), ("BOS", "LAX", 2611),
        ("BOS", "SFO", 2704), ("ATL", "LAX", 1946), ("ATL", "DEN", 1199),
        ("DFW", "LAX", 1235), ("DFW", "DEN", 641), ("IAH", "LAX", 1374),
        ("MSP", "SEA", 1399), ("DEN", "JFK", 1626),
    ]
    
    # make all routes bidirectional
    routes = []
    for src, dst, dist in routes_one_way:
        routes.append((src, dst, dist))
        routes.append((dst, src, dist))
    
    return airports, routes, coords


def print_header(title):
    """Print a formatted section header."""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def demo_phase1():
    """Demonstrate Phase 1: Adjacency Matrix Implementation."""
    print_header("PHASE 1: Adjacency Matrix + Basic Algorithms")
    
    airports, routes, coords = load_real_airport_data()
    
    # build adjacency matrix
    print("\nBuilding adjacency matrix...")
    matrix = build_matrix(airports, routes)
    name_to_idx = {name: i for i, name in enumerate(airports)}
    
    print(f"✓ Graph built: {len(airports)} airports, {len(routes)} routes")
    print(f"✓ Matrix size: {len(matrix)}×{len(matrix)} = {len(matrix)**2} cells")
    
    # interactive query
    print("\n--- Path Finding Demo ---")
    src_name = "JFK"
    dst_name = "LAX"
    
    src = name_to_idx[src_name]
    dst = name_to_idx[dst_name]
    
    print(f"\nQuery: Find path from {src_name} to {dst_name}")
    
    # BFS
    print("\n1. BFS (Breadth-First Search):")
    steps = bfs_from_src(src, matrix)
    if steps[dst] < INF:
        print(f"   Result: Reachable in {steps[dst]} hops")
    else:
        print(f"   Result: Not reachable")
    
    # DFS
    print("\n2. DFS (Depth-First Search):")
    visited, order = dfs_from_src(src, matrix)
    if visited[dst]:
        print(f"   Result: Destination reachable")
        print(f"   Traversal order: {[airports[i] for i in order[:5]]}... (showing first 5)")
    else:
        print(f"   Result: Not reachable")
    
    # Dijkstra
    print("\n3. Dijkstra's Algorithm:")
    dist, prev = dijkstra_from_src(src, matrix)
    path_indices = reconstruct_Dijkstra(src, dst, prev)
    
    if path_indices:
        path_names = [airports[i] for i in path_indices]
        print(f"   Shortest path: {' → '.join(path_names)}")
        print(f"   Total distance: {dist[dst]:.0f} miles")
    else:
        print(f"   Result: No path found")


def demo_phase2():
    """Demonstrate Phase 2: Adjacency List + Optimized Algorithms."""
    print_header("PHASE 2: Adjacency List + Optimized Algorithms + A*")
    
    airports, routes, coords = load_real_airport_data()
    
    # build adjacency list
    print("\nBuilding adjacency list...")
    adj, name_to_idx = build_adj_list(airports, routes)
    coords_idx = build_coords_idx(airports, coords)
    
    # calculate sparsity
    total_edges = sum(len(neighbors) for neighbors in adj)
    possible_edges = len(airports) * (len(airports) - 1)
    density = total_edges / possible_edges
    
    print(f"✓ Graph built: {len(airports)} airports")
    print(f"✓ Actual edges: {total_edges}")
    print(f"✓ Possible edges: {possible_edges}")
    print(f"✓ Graph density: {density*100:.1f}% (sparse!)")
    
    # interactive query
    src_name = "BOS"
    dst_name = "SFO"
    
    src = name_to_idx[src_name]
    dst = name_to_idx[dst_name]
    
    print(f"\n--- Optimized Path Finding: {src_name} to {dst_name} ---")
    
    # Dijkstra (optimized)
    print("\n1. Dijkstra (Optimized with Adjacency List):")
    dist, prev = dijkstra_from_src_list(src, adj)
    path = reconstruct_path(src, dst, prev)
    
    if path:
        path_names = [airports[i] for i in path]
        print(f"   Path: {' → '.join(path_names)}")
        print(f"   Distance: {dist[dst]:.0f} miles")
    
    # A* 
    print("\n2. A* Search (with geographic heuristic):")
    g, prev_a = astar(src, dst, adj, coords_idx)
    path_a = reconstruct_path(src, dst, prev_a)
    
    if path_a:
        path_names_a = [airports[i] for i in path_a]
        print(f"   Path: {' → '.join(path_names_a)}")
        print(f"   Distance: {g[dst]:.0f} miles")
        print(f"   Note: A* uses straight-line distance as heuristic")


def demo_comparison():
    """Show key performance differences."""
    print_header("PERFORMANCE COMPARISON: Phase 1 vs Phase 2")
    
    print("\nKey Differences:")
    print("\n┌─────────────────────┬──────────────────┬──────────────────┐")
    print("│ Aspect              │ Phase 1 (Matrix) │ Phase 2 (List)   │")
    print("├─────────────────────┼──────────────────┼──────────────────┤")
    print("│ Data Structure      │ 2D Array         │ Adjacency List   │")
    print("│ Space Complexity    │ O(V²)            │ O(V + E)         │")
    print("│ BFS Time            │ O(V²)            │ O(V + E)         │")
    print("│ Dijkstra Time       │ O(V² log V)      │ O((V+E) log V)   │")
    print("│ Best For            │ Dense graphs     │ Sparse graphs    │")
    print("└─────────────────────┴──────────────────┴──────────────────┘")
    
    print("\nFor our airport network (sparse graph):")
    print("  • V = 500 airports, E ≈ 15,000 routes")
    print("  • Matrix checks: 500² = 250,000 per node")
    print("  • List checks: ~30 neighbors per node")
    print("  • Expected speedup: ~40× on large datasets!")
    
    print("\nRun benchmark.py to see actual performance measurements.")


def interactive_menu():
    """Interactive menu for live demonstrations."""
    print_header("AIRPORT ROUTE OPTIMIZATION SYSTEM")
    print("                ECE590 Fall 2025")
    
    while True:
        print("\n" + "-" * 70)
        print("DEMONSTRATION MENU:")
        print("-" * 70)
        print("  1. Phase 1 Demo (Matrix + BFS/DFS/Dijkstra)")
        print("  2. Phase 2 Demo (List + Optimized Algorithms + A*)")
        print("  3. Performance Comparison Summary")
        print("  4. Run All Demos")
        print("  0. Exit")
        print("-" * 70)
        
        choice = input("\nSelect option (0-4): ").strip()
        
        if choice == "1":
            demo_phase1()
        elif choice == "2":
            demo_phase2()
        elif choice == "3":
            demo_comparison()
        elif choice == "4":
            print("\n" + ">" * 70)
            print("RUNNING ALL DEMONSTRATIONS")
            print(">" * 70)
            demo_phase1()
            demo_phase2()
            demo_comparison()
            print("\n" + "<" * 70)
            print("ALL DEMONSTRATIONS COMPLETE")
            print("<" * 70)
        elif choice == "0":
            print("\n" + "=" * 70)
            print("  Thank you for using the Airport Route System!")
            print("=" * 70)
            break
        else:
            print("\nInvalid option. Please choose 0-4.")
        
        input("\n[Press Enter to continue...]")


def main():
    """Main entry point."""
    try:
        interactive_menu()
    except KeyboardInterrupt:
        print("\n\nExiting... Goodbye!")
        sys.exit(0)


if __name__ == "__main__":
    main()
