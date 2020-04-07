package GraphTheory;

public class Vertex<E> {

    public E val;
    public int dist;
    public Vertex<E> prev;
    public Color color;

    public Vertex(E val) {
        this.val = val;
    }

}
