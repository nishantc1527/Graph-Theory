# --------------------------------------------------------
# This file is used to test all the algorithms performed
# on the graph's
# --------------------------------------------------------

from Graph import *


print("Depth First Search")
graph = DirectedGraph()  # prints the shortest path from source to target in a directed graph using
# breadth-first-search algorithm
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)
graph.connect(1, 2, 0)  # connects vertex 1 to 2
graph.connect(2, 3, 0)  # connects vertex 2 to 3
graph.connect(4, 3, 0)  # connects vertex 4 to 3
graph.connect(5, 4, 0)  # connects vertex 5 to 4
graph.connect(1, 5, 0)  # connects vertex 1 to 5
graph.connect(5, 2, 0)  # connects vertex 2 to 5
print_in_dfs(graph, 1)

# 1 -> 2 -> 3
# ↓  ↑      ↑
# 5 <- 4 ->


print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


print("Breadth First Search")
graph = DirectedGraph()  # prints the shortest path from source to target in a directed graph using
# breadth-first-search algorithm
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)
graph.connect(1, 2, 0)  # connects vertex 1 to 2
graph.connect(2, 3, 0)  # connects vertex 2 to 3
graph.connect(3, 4, 0)  # connects vertex 4 to 3
graph.connect(4, 5, 0)  # connects vertex 5 to 4
graph.connect(1, 5, 0)  # connects vertex 1 to 5
graph.connect(5, 2, 0)  # connects vertex 2 to 5
print_in_bfs(graph, 1)

# 1 -> 2 -> 3
# ↓  ↑      ↓
# 5 <- 4 <-


print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


print("Shortest Path Breadth First Search")
graph = DirectedGraph()  # prints the shortest path from source to target in a directed graph using
# breadth-first-search algorithm
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)
graph.connect(1, 2, 0)  # connects vertex 1 to 2
graph.connect(2, 3, 0)  # connects vertex 2 to 3
graph.connect(3, 4, 0)  # connects vertex 4 to 3
graph.connect(4, 5, 0)  # connects vertex 5 to 4
graph.connect(1, 5, 0)  # connects vertex 1 to 5
graph.connect(5, 2, 0)  # connects vertex 2 to 5
print_shortest_path_bfs(graph, 1, 2)

# 1 -> 2 -> 3
# ↓  ↑      ↓
# 5 <- 4 <-


print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


print("Shortest Path Dikstra")
graph = WeightedGraph()  # prints the shortest path from source to target in a weighted graph using dikstra algorithm
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)
graph.connect(1, 2, 6)  # connects vertex 1 to 2 with weight of 6
graph.connect(2, 3, 5)  # connects vertex 2 to 3 with weight of 5
graph.connect(3, 4, 2)  # connects vertex 4 to 3 with weight of 2
graph.connect(4, 5, 3)  # connects vertex 5 to 4 with weight of 3
graph.connect(1, 5, 1)  # connects vertex 1 to 5 with weight of 1
graph.connect(5, 2, 1)  # connects vertex 2 to 5 with weight of 1
print_shortest_path_dikstra(graph, 1, 2)

# 1 -> 2: 6
# 2 -> 3: 5
# 3 -> 4: 2
# 4 -> 5: 3
# 1 -> 5: 1
# 5 -> 2: 1

# 1 -> 2 -> 3
# ↓  ↑      ↓
# 5 <- 4 <-


print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


print("Shortest Path Bellam Ford")
graph = WeightedGraph()  # prints the shortest path from source to target in a weighted graph using bellman ford
# algorithm
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)
graph.connect(1, 2, 6)  # connects vertex 1 to 2 with weight of 6
graph.connect(2, 3, 5)  # connects vertex 2 to 3 with weight of 5
graph.connect(3, 4, 2)  # connects vertex 4 to 3 with weight of 2
graph.connect(4, 5, 3)  # connects vertex 5 to 4 with weight of 3
graph.connect(1, 5, 1)  # connects vertex 1 to 5 with weight of 1
graph.connect(5, 2, 1)  # connects vertex 2 to 5 with weight of 1
print_shortest_path_bellman_ford(graph, 1, 2)

# 1 -> 2: 6
# 2 -> 3: 5
# 3 -> 4: 2
# 4 -> 5: 3
# 1 -> 5: 1
# 5 -> 2: 1

# 1 -> 2 -> 3
# ↓  ↑      ↓
# 5 <- 4 <-


print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


print("Shortest Path Bellman Ford Optimized")
graph = WeightedGraph()  # prints the shortest path from source to target in a weighted graph using bellman ford
# algorithm
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)
graph.connect(1, 2, 6)  # connects vertex 1 to 2 with weight of 6
graph.connect(2, 3, 5)  # connects vertex 2 to 3 with weight of 5
graph.connect(3, 4, 2)  # connects vertex 4 to 3 with weight of 2
graph.connect(4, 5, 3)  # connects vertex 5 to 4 with weight of 3
graph.connect(1, 5, 1)  # connects vertex 1 to 5 with weight of 1
graph.connect(5, 2, 1)  # connects vertex 2 to 5 with weight of 1
print_shortest_path_bellman_ford_optimized(graph, 1, 2)

# 1 -> 2: 6
# 2 -> 3: 5
# 3 -> 4: 2
# 4 -> 5: 3
# 1 -> 5: 1
# 5 -> 2: 1

# 1 -> 2 -> 3
# ↓  ↑      ↓
# 5 <- 4 <-
