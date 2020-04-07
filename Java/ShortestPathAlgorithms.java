package GraphTheory;

import java.util.HashSet;
import java.util.LinkedList;

public class ShortestPathAlgorithms {

    private static <E> void initializeSingleSource(WeightedGraphAdjacencyList<E> graph, E source) {
        for(Vertex vertex : graph.vertices.values()) {
            vertex.color = Color.white;
            vertex.dist = Integer.MAX_VALUE;
            vertex.prev = null;
        }

        graph.getVertex(source).dist = 0;
    }

    public static <E> void bellmanFordShortestPathAdjacencyList(WeightedGraphAdjacencyList<E> graph, E source) {
        initializeSingleSource(graph, source);
        int size = graph.vertices.size();

        for(int i = 0; i < size - 1; i ++) {
            for(E value : graph.vertices.keySet()) {
                Vertex<E> vertexForm = graph.vertices.get(value);
                long currWeight = vertexForm.dist;

                for(E adjacent : graph.adjacencyList.get(value)) {
                    Vertex<E> currVertexForm = graph.vertices.get(adjacent);

                    if(currWeight + graph.weights.get(graph.getEdge(value, adjacent)) < currVertexForm.dist) {
                        currVertexForm.dist = currWeight + graph.weights.get(graph.getEdge(value, adjacent));
                        currVertexForm.prev = vertexForm;
                    }
                }
            }
        }
    }

    public static <E> void dikstraShortestPathAdjacencyList(WeightedGraphAdjacencyList<E> graph, E source) {
        initializeSingleSource(graph, source);
        HashSet<Vertex<E>> visited = new HashSet<>();
        int size = graph.vertices.size();

        while(visited.size() != size) {
            Vertex<E> min = new Vertex<>(null);
            min.dist = Integer.MAX_VALUE;

            for(Vertex vertex : graph.vertices.values()) {
                if(!visited.contains(vertex) && vertex.dist < min.dist) {
                    min = vertex;
                }
            }

            LinkedList<E> neighbors = graph.adjacencyList.get(min.val);

            if(neighbors == null) {
                break;
            }

            for(E val : neighbors) {
                Vertex<E> vertexForm = graph.getVertex(val);

                if(min.dist + graph.weights.get(graph.getEdge(min.val, val)) < vertexForm.dist) {
                    vertexForm.dist = min.dist + graph.weights.get(graph.getEdge(min.val, val));
                    vertexForm.prev = min;
                }
            }

            visited.add(min);
        }
    }

    public static void main(String[] args) {
        System.out.println("Shortest Path Algorithm Using Bellman Ford Algorithm");
        System.out.println();
        WeightedGraphAdjacencyList<Character> graph = new WeightedGraphAdjacencyList<>();

        graph.addVertex('a');
        graph.addVertex('b');
        graph.addVertex('c');
        graph.addVertex('d');
        graph.addVertex('e');

        graph.connect('a', 'b', 6);
        graph.connect('b', 'c', 5);
        graph.connect('d', 'c', 2);
        graph.connect('d', 'e', 4);
        graph.connect('a', 'e', 1);
        graph.connect('e', 'b', 1);

        bellmanFordShortestPathAdjacencyList(graph, 'a');

        for(Vertex vertex : graph.vertices.values()) {
            System.out.println(vertex + ": " + vertex.dist);
        }
        System.out.println();
        System.out.println();

        // a -> b -> c
        // ⬇ ↗    ↗
        // e <- d

        System.out.println("-------------------------------------------------------------------------------------------");

        System.out.println();
        System.out.println();
        System.out.println("Shortest Path Algorithm Using Dikstra Algorithm");
        System.out.println();
        graph = new WeightedGraphAdjacencyList<>();

        graph.addVertex('a');
        graph.addVertex('b');
        graph.addVertex('c');
        graph.addVertex('d');
        graph.addVertex('e');

        graph.connect('a', 'b', 6);
        graph.connect('b', 'c', 5);
        graph.connect('d', 'c', 2);
        graph.connect('d', 'e', 4);
        graph.connect('a', 'e', 1);
        graph.connect('e', 'b', 1);

        dikstraShortestPathAdjacencyList(graph, 'a');

        for(Vertex vertex : graph.vertices.values()) {
            System.out.println(vertex + ": " + vertex.dist);
        }

        // a -> b -> c
        // ⬇ ↗    ↗
        // e <- d
    }


}
