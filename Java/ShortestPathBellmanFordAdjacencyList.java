package GraphTheory;

public class ShortestPathBellmanFordAdjacencyList {

    private static <E> void initializeSingleSource(WeightedGraphAdjacencyList<E> graph, E source) {
        for(Vertex vertex : graph.vertices.values()) {
            vertex.color = Color.white;
            vertex.dist = Integer.MAX_VALUE;
            vertex.prev = null;
        }

        graph.getVertex(source).dist = 0;
    }

    public static <E> void shortestPathAdjacencyList(WeightedGraphAdjacencyList<E> graph, E source) {
        initializeSingleSource(graph, source);
        int size = graph.vertices.size();

        for(int i = 0; i < size - 1; i ++) {

        }
    }

}
