import math


class Vertex:
    def __init__(self, val):
        self.val = val
        self.dist = None
        self.prev = None
        self.color = None

    def __str__(self):
        return str(self.val)


class Graph:
    def __init__(self):
        pass

    def add_vertex(self, val):
        pass

    def connect(self, val1, val2, weight):
        pass

    def get(self, val):
        pass


class DirectedGraph(Graph):
    def __init__(self):
        Graph.__init__(self)
        self.adj = {}  # adjacency list
        self.vertices = {}  # stores the references to all vertices

    def add_vertex(self, val):
        self.adj[val] = []  # initialize val's adjacency list
        self.vertices[val] = Vertex(val)  # set val's reference to curr

    def connect(self, val1, val2, weight):
        self.adj[val1].append(val2)  # add the vertex form of val2 to val1's adjacency
        # list

    def get(self, val):
        return self.vertices[val]  # return the vertex form of val according to vertices


class WeightedGraph(Graph):
    def __init__(self):
        Graph.__init__(self)
        self.adj = {}  # adjacency list
        self.weights = {}  # stores the weights of all edges
        self.vertices = {}  # stores the reference of all vertices

    def add_vertex(self, val):
        self.vertices[val] = Vertex(val)  # add the vertex to vertices
        self.adj[val] = []  # set the adjacency list of val to empty

    def connect(self, val1, val2, weight):
        self.adj[val1].append(val2)  # add vertex form of val2 to val1's adjacency list
        self.weights[val1, val2] = weight  # add the edge made to weights

    def get(self, val):
        return self.vertices[val]  # returns the vertex form of a value


def init_graph(directed_graph, source):  # resets all attributes
    for v in directed_graph.vertices.values():
        v.prev = None
        v.color = 0
        v.dist = math.inf
    graph.get(source).dist = 0


def shortest_path_bfs_initializer(directed_graph, source):
    # color: 0 means white, 1 mean grey, 2 means black
    # white means not visited, grey means visited, black means visited and all neighbors are visited

    init_graph(directed_graph, source)
    queue = [graph.get(source)]  # initializes color and prev values of all vertices to nothing, and the
    # queue used to perform breadth-first-search
    while not len(queue) == 0:
        curr = queue.pop(0)
        curr.color = 1
        # set color to grey, meaning current vertex is visited

        for v in directed_graph.adj[curr.val]:
            vertex_form = directed_graph.get(v)
            if vertex_form.color == 0:  # if not already visited, add it to queue
                vertex_form.prev = curr
                vertex_form.dist = curr.dist + 1
                queue.append(vertex_form)

        # all neighbors are visited, so update color to black

        curr.color = 2


# Can be called only after bfs with source as the start is called


def shortest_path_bfs(directed_graph, source, target):
    shortest_path_bfs_initializer(directed_graph, source)  # initializes the prev and color values of all vertices
    ans = []
    source = directed_graph.get(source)
    target = directed_graph.get(target)  # initialize the vertex form of inputs
    while target is not source:
        ans.append(target)
        target = target.prev  # work backwards using prev values

    ans.append(source)
    ans.reverse()  # since stored in reverse order of the path, reverse the final answer
    return ans


def print_shortest_path(directed_graph, source, target):
    path = shortest_path_bfs(directed_graph, source, target)
    for i in range(len(path) - 1):
        print(path[i], "->", end=" ")
    print(path[len(path) - 1])


def initialize_single_source(weighted_graph, source):  # initialize all attributes for every vertex in graph
    # initially, the prev values are None since you don't know where they come from, color is 0 (white) because they
    # aren't visited yet, and dist is infinity because you don't know a path from source to that vertex
    for v in weighted_graph.vertices.values():
        v.prev = None
        v.color = 0
        v.dist = math.inf
    weighted_graph.get(source).dist = 0  # the distance from source to source is 0


def shortest_path_dikstra(weighted_graph, source):
    initialize_single_source(weighted_graph, source)
    visited = set()
    size = len(weighted_graph.vertices)  # initialize all attributes, and keep a set to keep track of all visited
    # vertices so far
    while size is not len(visited):  # loop until you visited all vertices
        minimum_vertex = Vertex(0)
        minimum_vertex.dist = math.inf
        for v in weighted_graph.vertices.values():
            if v not in visited and v.dist < minimum_vertex.dist:
                minimum_vertex = v
        curr_weight = minimum_vertex.dist  # get the vertex with the smallest path calculated that's not visited yet,
        # and find the weight from the source to that vertex calculated so far
        for neighbor in weighted_graph.adj[minimum_vertex.val]:  # traverse every vertex neighboring selected vertex
            vertex_form = weighted_graph.get(neighbor)  # store the vertex form of each neighbor
            if curr_weight + weighted_graph.weights[minimum_vertex.val, vertex_form.val] < vertex_form.dist:  #
                vertex_form.dist = curr_weight + weighted_graph.weights[minimum_vertex.val, vertex_form.val]
                vertex_form.prev = minimum_vertex  # update the minimum path if needed from minimum_vertex to all of
                # it's neighbors and if needed, set the prev value
        visited.add(minimum_vertex)  # add the vertex selected to the visited set


def shortest_path_bellman_ford(weighted_graph, source):
    initialize_single_source(weighted_graph, source)
    visited = set()
    visited.add(weighted_graph.get(source))
    for i in range(len(weighted_graph.vertices) - 1):  # loop the total amount of vertices - 1 times
        for v in weighted_graph.vertices.values():
            if v in visited:  # check if visited already
                neighbors = weighted_graph.adj[v.val]
                curr_weight = v.dist  # get neighbors and find the minimum weight found so far
                for neighboring_vertex in neighbors:
                    vertex_form = weighted_graph.get(neighboring_vertex)
                    if curr_weight + weighted_graph.weights[v.val, neighboring_vertex] < vertex_form.dist:
                        visited.add(vertex_form)
                        vertex_form.dist = curr_weight + weighted_graph.weights[v.val, neighboring_vertex]
                        vertex_form.prev = v  # check every neighbor and see if you can improve the weight, and if
                        # you can, set the prev value too


graph = WeightedGraph()
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
print_shortest_path(graph, 1, 2)

# 1 -> 2: 6
# 2 -> 3: 5
# 3 -> 4: 2
# 4 -> 5: 3
# 1 -> 5: 1
# 5 -> 2: 1

# 1 -> 2 -> 3
# ↓  ↑      ↑
# 5 <- 4 ->
