package GraphTheory.ShortestPathAlgorithms;

import GraphTheory.Vertex;
import GraphTheory.WeightedGraphAdjacencyList;

public class BellmanFordShortestPath {

    private static <E> void initializeSingleSource(WeightedGraphAdjacencyList<E> graph, E source) {
        for(Vertex vertex : graph.vertices.values()) {
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

}
