package GraphTheory;

import java.util.HashMap;
import java.util.LinkedList;

public class WeightedGraphAdjacencyList<E> implements GraphAdjacencyList<E> {

    public HashMap<E, LinkedList<E>> adjacencyList;
    public HashMap<E, Vertex<E>> vertices;
    public HashMap<Edge<E>, Integer> weights;
    public HashMap<Pair<E, E>, Edge<E>> edges;

    @Override
    public void addVertex(E val) {
        vertices.putIfAbsent(val, new Vertex<>(val));
        adjacencyList.putIfAbsent(val, new LinkedList<>());
    }

    @Override
    public void connect(E val1, E val2, Integer... weight) {
        adjacencyList.getOrDefault(val1, new LinkedList<>()).add(val2);
        weights.putIfAbsent(new Edge<>(val1, val2), weight[0]);
    }

    @Override
    public Vertex getVertex(E val) {
        return vertices.getOrDefault(val, null);
    }

    @Override
    public Edge getEdge(E val1, E val2) {
        return edges.getOrDefault(new Pair<>(val1, val2), null);
    }

}
