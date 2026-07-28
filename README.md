# Uninformed Search Algorithms

Complete Python implementation of 5 uninformed search algorithms with test cases, visualization and comparison.

## 📋 Implemented algorithms

### 1. **BFS (Breadth-First Search)**
- **File**: `algorithms/bfs.py`
- **Structure**: Queue (FIFO)
- **Properties**:
  - ✓ Complete (finds a solution if one exists)
  - ✓ Optimal (in terms of number of edges)
  - Use: Find the shortest path in terms of steps

### 2. **DFS (Depth-First Search)**
- **File**: `algorithms/dfs.py`
- **Structure**: Stack (LIFO)
- **Properties**:
  - ✓ Complete (on finite graphs)
  - ✗ NOT optimal
  - Use: Exhaustive exploration, cycle detection

### 3. **DLS (Depth-Limited Search)**
- **File**: `algorithms/dls.py`
- **Structure**: Stack with a depth limit
- **Properties**:
  - ✓ Complete if the solution is within the limit
  - ✗ NOT optimal
  - Use: Limit search on infinite graphs

### 4. **IDS (Iterative Deepening Search)**
- **File**: `algorithms/ids.py`
- **Structure**: Repeated DLS with incremental limits
- **Properties**:
  - ✓ Complete
  - ✓ Optimal (combines the advantages of BFS and DFS)
  - Use: Very large spaces where BFS uses too much memory

### 5. **UCS (Uniform-Cost Search)**
- **File**: `algorithms/ucs.py`
- **Structure**: Priority queue
- **Properties**:
  - ✓ Complete
  - ✓ Optimal in total cost
  - Use: Weighted graphs, find the lowest-cost path

## 📁 Project structure

```
search-algorithms/
├── algorithms/           # Module with the algorithms
│   ├── __init__.py
│   ├── bfs.py           # Breadth-First Search
│   ├── dfs.py           # Depth-First Search
│   ├── dls.py           # Depth-Limited Search
│   ├── ids.py           # Iterative Deepening Search
│   └── ucs.py           # Uniform-Cost Search
│
├── problems/            # Module with test cases
│   ├── __init__.py
│   ├── graph.py        # Graph class
│   └── test_cases.py   # Predefined test cases
│
├── main.py             # Main program
├── visualization.py    # Visualization module
├── requirements.txt    # Dependencies
└── README.md          # This file
```

## 🚀 Installation and usage

### Prerequisites
- Python 3.8+
- No external dependencies (uses the standard library)

### Installation
```bash
# Clone or download the project
cd search-algorithms

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies (even though they are only standard libraries)
pip install -r requirements.txt
```

### Running
```bash
# Run the main program
python main.py

# Follow the instructions in the interactive menu
```

## 🧪 Test cases

### 1. Simple graph
Simple 6-node network for quick tests:
```
    A --- B --- D
    |     |     |
    C --- E --- F
```

**Use**: Quick functionality check

### 2. City route
Graph representing Spanish cities connected with real distances:
```
Madrid ←→ Barcelona
  ↓         ↓
Valencia ←→ Tarragona
  ↓
Alicante
```

**Use**: Route-search problem with costs

### 3. Map with costs
Tree with variable edge weights:
```
        A
       / \
      B   C
     /|   |\
    D E   F G
```

**Use**: Comparison of optimal vs non-optimal algorithms

### 4. Maze
3×4 matrix where 1 = valid path, 0 = wall:
```
1 1 0 1
0 1 1 1
1 1 0 1
```

**Use**: Search problem in discrete state spaces

## 📊 Main features

### For each search it returns:
1. **Found path**: List of nodes from start to goal
2. **Explored nodes**: Set of all visited nodes
3. **Total cost**: (UCS only) Sum of the path weights
4. **Execution time**: Measured in milliseconds

### Visualization:
- Graph information (nodes, edges)
- Detailed result per algorithm
- Comparison table with all algorithms
- ANSI colors for better readability

## 📈 Example output

```
==================================================
  CITY ROUTE  
==================================================

📊 Graph information: City Route
   Nodes: Madrid, Barcelona, Valencia, Alicante, Tarragona
   Total nodes: 5
   Total edges: 5

▶ BFS (Breadth-First Search):
✓ Path found:
  Madrid → Valencia → Alicante
  Path length: 3
  Explored nodes: 3
  Explored nodes: Madrid, Valencia, Alicante
  
[... results of other algorithms ...]

================================================================================
ALGORITHM COMPARISON
================================================================================

Algorithm               | Path found | Explored nodes | Cost     | Time (ms)
────────────────────────────────────────────────────────────────────────────────────
BFS                    | Yes               | 3                | N/A      | 0.0234
DFS                    | Yes               | 3                | N/A      | 0.0156
DLS                    | Yes               | 3                | N/A      | 0.0189
IDS                    | Yes               | 5                | N/A      | 0.0312
UCS                    | Yes               | 3                | 560.00   | 0.0401
```

## 🔄 Algorithm comparison

| Algorithm | Complete | Optimal | Memory | Time   | Best for |
|-----------|----------|---------|--------|--------|----------|
| BFS       | ✓        | ✓       | High   | Medium | Small graphs |
| DFS       | ✓        | ✗       | Low    | Fast   | Exhaustive search |
| DLS       | Partial  | ✗       | Low    | Fast   | Limiting depth |
| IDS       | ✓        | ✓       | Medium | Medium | Large spaces |
| UCS       | ✓        | ✓       | High   | Slow   | Weighted graphs |

## 💡 Important notes

### BFS vs DFS
- **BFS**: Guarantees the shortest path (number of steps)
- **DFS**: More memory-efficient, but does not guarantee optimality

### IDS vs BFS
- **IDS**: Uses less memory than BFS
- **BFS**: Faster than IDS
- Both find the optimal solution

### UCS vs BFS
- **BFS**: Optimal only if all costs are equal
- **UCS**: Optimal with any positive cost

### DLS and limits
- Useful when you know where to search
- Avoids infinite search on cyclic graphs

## 🎓 Educational concepts

The project demonstrates:
- Data structures (queue, stack, heap)
- Path reconstruction
- Search metrics
- Comparative analysis
- Algorithm visualization

## ✅ Requirements checklist

- [x] Implement BFS correctly
- [x] Implement DFS correctly
- [x] Implement DLS with a depth limit
- [x] Implement IDS with limit iteration
- [x] Implement UCS with a priority queue
- [x] Define initial and goal state
- [x] Visualize the found route
- [x] Show explored nodes
- [x] Report total cost (UCS)
- [x] Compare results across algorithms
- [x] Use suitable structures for each algorithm
- [x] Multiple test cases
- [x] Complete documentation

## 📝 License

This project is for educational use.

## 👨‍💻 Author

Implementation of search algorithms for educational purposes.

---

**Enjoy exploring search algorithms!** 🎯

## Applications

In [`aplicaciones/entrega_paquetes.ipynb`](aplicaciones/entrega_paquetes.ipynb)
the package's algorithms are applied to a real problem: planning package delivery
by comparing classic search strategies. The notebook includes the executed results.
