# --------------------------------------------------------
# This file is used to test all the algorithms performed
# on the graph's
# --------------------------------------------------------

from Graph import *
from colorama import Fore, Style


print("Depth First Search")

print(Fore.BLUE)
print("-----------------------")
print("Graph:")
print("1 -> 2 -> 3")
print("↓  ↗   ↗")
print("5 -> 4")
print()
print("Source:")
print("1")
print("-----------------------")
print(Style.RESET_ALL)

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


print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


print("Breadth First Search")

print(Fore.BLUE)
print("-----------------------")
print("Graph:")
print("1 -> 2 -> 3")
print("↓  ↗   ↗")
print("5 -> 4")
print()
print("Source:")
print("1")
print("-----------------------")
print(Style.RESET_ALL)

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


print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


print("Shortest Path Breadth First Search")

print(Fore.BLUE)
print("-----------------------")
print("Graph:")
print("1 -> 2 -> 3")
print("↓  ↗   ↗")
print("5 <- 4")
print()
print("Source:")
print("1")
print()
print("Target")
print("2")
print("-----------------------")
print(Style.RESET_ALL)

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


print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


print("Shortest Path Dikstra")

print(Fore.BLUE)
print("-----------------------")
print("Weights")
print("1 -> 2: 6")
print("2 -> 3: 5")
print("3 -> 4: 2")
print("4 -> 5: 3")
print("1 -> 5: 1")
print("5 -> 2: 1")
print()
print("Graph:")
print("1 -> 2 -> 3")
print("↓  ↗   ↗")
print("5 -> 4")
print()
print("Source:")
print("1")
print()
print("Target")
print("2")
print("-----------------------")
print(Style.RESET_ALL)


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


print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


print("Shortest Path Bellman Ford")

print(Fore.BLUE)
print("-----------------------")
print("Weights")
print("1 -> 2: 6")
print("2 -> 3: 5")
print("3 -> 4: 2")
print("4 -> 5: 3")
print("1 -> 5: 1")
print("5 -> 2: 1")
print()
print("Graph:")
print("1 -> 2 -> 3")
print("↓  ↗   ↗")
print("5 -> 4")
print()
print("Source:")
print("1")
print()
print("Target")
print("2")
print("-----------------------")
print(Style.RESET_ALL)

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


print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


print("Shortest Path Bellman Ford Optimized Using Depth First Search")

print(Fore.BLUE)
print("-----------------------")
print("Weights")
print("1 -> 2: 6")
print("2 -> 3: 5")
print("3 -> 4: 2")
print("4 -> 5: 3")
print("1 -> 5: 1")
print("5 -> 2: 1")
print()
print("Graph:")
print("1 -> 2 -> 3")
print("↓  ↗   ↗")
print("5 -> 4")
print()
print("Source:")
print("1")
print()
print("Target")
print("2")
print("-----------------------")
print(Style.RESET_ALL)


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
print_shortest_path_bellman_ford_optimized_dfs(graph, 1, 2)


print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
