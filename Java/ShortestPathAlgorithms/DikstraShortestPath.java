package GraphTheory.ShortestPathAlgorithms;

import GraphTheory.Vertex;
import GraphTheory.WeightedGraphAdjacencyList;

import java.util.HashSet;
import java.util.LinkedList;

public class DikstraShortestPath {

    private static <E> void initializeSingleSource(WeightedGraphAdjacencyList<E> graph, E source) {
        for(Vertex vertex : graph.vertices.values()) {
            vertex.dist = Integer.MAX_VALUE;
            vertex.prev = null;
        }

        graph.getVertex(source).dist = 0;
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

}
