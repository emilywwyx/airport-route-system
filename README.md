# Airport-Route-System

**Programming Assignment: Graph Algorithms & Performance Analysis**

> You are expected to complete this work via pair programming. If you're unfamiliar with pair programming, please Google.

## Overview

Build an airport route optimization system that finds paths between airports. You will implement graph representations and path-finding algorithms, then analyze and optimize their performance.

This is a **three-phase assignment**. Each phase builds upon the previous with stricter performance requirements.

## Problem Description

You are building a route planning system for an airline consortium. The system must find routes between airports efficiently. Your implementation will be tested against increasingly large datasets with strict time limits.

### Datasets

| Dataset | Airports | Routes | Time Limit |
|---------|----------|--------|------------|
| Small   | 24       | ~200   | No limit   |
| Medium  | 200      | ~3,000 | < 100ms    |
| Large   | 500      | ~15,000| < 50ms     |

## Phase 1: Baseline Implementation

Implement the graph and path-finding algorithms. This establishes your baseline for performance comparison.

### Requirements

1. **Graph Representation:** Implement using an adjacency matrix.
2. **BFS:** Implement Breadth-First Search.
3. **DFS:** Implement Depth-First Search.
4. **Dijkstra:** Implement Dijkstra's shortest path algorithm.
5. **Performance Logging:** Record and report execution times.

## Phase 2: Optimized Implementation

Refactor your implementation to meet the performance requirements for larger datasets. You must identify the bottlenecks in Phase 1 and choose appropriate data structures to address them.

### Requirements

1. **Graph Representation:** Choose a representation suitable for sparse graphs.
2. **Algorithm Optimization:** Optimize each algorithm to achieve better time complexity.
3. **A\* Search:** Implement A* search with an appropriate heuristic for geographic routing.
4. **Performance Targets:** Your implementation must pass the automated benchmarks within the specified time limits.

## Phase 3: Analysis

### Empirical Analysis

1. Compare execution times between Phase 1 and Phase 2 implementations.
2. Analyze how performance scales with graph size.
3. Compare memory usage between implementations.
4. Calculate and report speedup factors.

### Advanced Features (Optional)

- K-shortest paths
- Constrained routing (maximum stops)
- Batch queries (single source to all destinations)

## Deliverables

### Code

| File | Description |
|------|-------------|
| `graph_matrix.py` | Phase 1 graph implementation |
| `graph_list.py` | Phase 2 graph implementation |
| `algorithms_v1.py` | Phase 1 algorithm implementations |
| `algorithms_v2.py` | Phase 2 algorithm implementations |
| `benchmark.py` | Performance testing |
| `main.py` | GUI application |

### Written Report

Your report (2-4 pages) must include:

1. **Complexity Analysis:** Derive and explain the time complexity of each implementation.
2. **Experimental Results:** Graphs comparing Phase 1 vs Phase 2 performance.
3. **Discussion:** Explain your optimization choices and their effects.
4. **Trade-offs:** When might your Phase 1 implementation be preferred?

## Academic Integrity

All code and written analysis must be your own. You may use Python's standard library but **no external graph libraries** (NetworkX, igraph, etc.). The autograder will check for code similarity.

## Submission

**Due Date:** 12/13/2025

1. Submit a ZIP file containing all Python files and your report PDF to **Canvas**.
2. **Continuously push changes to the GitHub repository provided to your team in ECE590-F25 Organization**

## Oral Presentation

**Date:** 12/14/2025

Each team will have 10 minutes.
