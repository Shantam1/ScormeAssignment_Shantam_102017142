
### 2. `main.py`

"""python

Assignment: Implement the most efficient algorithm to solve the given problem.

Problem Statement:
You are given a Directed Acyclic Graph (DAG) with `n` nodes, numbered from `0` to `n-1`.
The graph is represented as an adjacency list where `graph[i]` is a list of tuples `(j, w)`,
representing an edge from node `i` to node `j` with weight `w`. Your task is to find the longest
path in the graph starting from any node.

Function Signature:
def longest_path(graph: list) -> int:

Parameters:
- graph (list): A list of lists, where `graph[i]` contains tuples `(j, w)` representing an edge
  from node `i` to node `j` with weight `w`.

Returns:
- int: The length of the longest path in the graph.

Example:
>>> graph = [
...     [(1, 3), (2, 2)],
...     [(3, 4)],
...     [(3, 1)],
...     []
... ]
>>> longest_path(graph)
7
"""
from collections import defaultdict

def longest_path(graph: list) -> int:
    sorted_nodes = topological_sort(graph)
    return calculate_longest_path(graph, sorted_nodes)

# Helper function to perform topological sort
def topological_sort(graph):
    # Your implementation goes here
    visited = set()
    sorted_nodes = []

    def visit(node):
        if node not in visited:
            visited.add(node)
            for successor, _ in graph[node]:
                visit(successor)
            sorted_nodes.append(node)

    for node in range(len(graph)):
        if node not in visited:
            visit(node)

    return sorted_nodes[::-1]

# Function to calculate longest path using topological sort
def calculate_longest_path(graph, topo_order):
    dista = defaultdict(lambda: float('-inf'))

    for node in topo_order:
        if dista[node] == float('-inf'):
            dista[node] = 0

        for successor, weight in graph[node]:
            dista[successor] = max(dista[successor], dista[node] + weight)

    max_distance = max(dista.values())
    
    return max_distance if max_distance != float('-inf') else 0
