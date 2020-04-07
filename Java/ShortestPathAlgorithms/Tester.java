package GraphTheory.ShortestPathAlgorithms;


import GraphTheory.Vertex;
import GraphTheory.WeightedGraphAdjacencyList;

public class Tester {

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

        BellmanFordShortestPath.bellmanFordShortestPathAdjacencyList(graph, 'a');

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

        DikstraShortestPath.dikstraShortestPathAdjacencyList(graph, 'a');

        for(Vertex vertex : graph.vertices.values()) {
            System.out.println(vertex + ": " + vertex.dist);
        }

        // a -> b -> c
        // ⬇ ↗    ↗
        // e <- d
    }

}
