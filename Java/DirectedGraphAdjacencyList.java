package GraphTheory;

import java.util.HashMap;
import java.util.LinkedList;

public class DirectedGraph<E> implements Graph<E> {

    public HashMap<E, LinkedList<E>> adjacencyList;
    public HashMap<E, Vertex<E>> vertices;

    @Override
    public void addVertex(E val) {
        vertices.putIfAbsent(val, new Vertex<>(val));
        adjacencyList.putIfAbsent(val, new LinkedList<>());
    }

    @Override
    public void connect(E val1, E val2, Integer... weight) {
        adjacencyList.getOrDefault(val1, new LinkedList<>()).add(val2);
    }

    @Override
    public Vertex getVertex(E val) {
        return vertices.getOrDefault(val, null);
    }

    @Override
    public Edge getEdge(E val1, E val2) {
        return null;
    }

}
