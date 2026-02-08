# Airport Route System

A Python-based airport route optimization system that models airline networks as graphs and evaluates multiple path-finding algorithms under different performance constraints.

This project explores how graph representation choices and algorithmic optimizations affect scalability, runtime, and memory usage when routing between airports.

---

## Project Overview

The Airport Route System computes routes between airports using classical graph algorithms and compares their performance across datasets of increasing size.

Two implementations are provided:

- **Baseline implementation** using adjacency matrices
- **Optimized implementation** using data structures suitable for sparse graphs

The system is designed to support both shortest-path queries and performance benchmarking under realistic airline network sizes.

---

## Problem Setting

Airports are modeled as graph nodes and flight routes as edges.  
The system must efficiently compute routes as the network grows from small to large scale.

### Dataset Scale

| Dataset | Airports | Routes | Characteristics |
|--------|----------|--------|----------------|
| Small  | 24       | ~200   | Development & correctness |
| Medium| 200      | ~3,000 | Performance-sensitive |
| Large | 500      | ~15,000| Stress testing & optimization |

---

## Implementation Phases

### Phase 1: Baseline System

A straightforward implementation to establish correctness and baseline performance.

**Features**
- Adjacency matrix graph representation
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Dijkstra’s shortest path algorithm
- Execution time logging for comparison

---

### Phase 2: Optimized System

A refactored version focused on scalability and runtime efficiency.

**Improvements**
- Adjacency list representation for sparse graphs
- Optimized algorithm implementations
- A* search with heuristic-based routing
- Designed to meet strict runtime constraints on large datasets

---

### Phase 3: Performance Analysis

A detailed empirical evaluation comparing the two implementations.

**Analysis includes**
- Runtime comparison across dataset sizes
- Scaling behavior as graph size increases
- Memory usage trade-offs
- Speedup calculations between implementations

---

## Project Structure

| File | Description |
|------|------------|
| `graph_matrix.py` | Adjacency matrix graph (baseline) |
| `graph_list.py` | Adjacency list graph (optimized) |
| `algorithms_v1.py` | Baseline algorithms |
| `algorithms_v2.py` | Optimized algorithms |
| `benchmark.py` | Performance benchmarking |
| `main.py` | Application entry point |

---

## Key Features

- Modular graph representations
- Multiple path-finding strategies
- Performance benchmarking framework
- Extensible design for advanced routing features

### Optional Extensions
- K-shortest paths
- Constrained routing (e.g., max stops)
- Batch routing queries

---

## Technical Notes

- Implemented in **Python**
- Uses only the Python standard library
- No external graph libraries (e.g., NetworkX)

---

## Motivation

This project demonstrates how algorithmic choices and data structures directly impact real-world system performance. It highlights trade-offs between simplicity, memory usage, and scalability in graph-based systems.

---

## License

This project is provided for educational and research purposes.
