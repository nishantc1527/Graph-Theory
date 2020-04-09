package GraphTheory;

import java.util.Objects;

public class Vertex<E> {

    public E val;
    public long dist;
    public Vertex<E> prev;
    public Color color;

    public Vertex(E val) {
        this.val = val;
    }

    @Override
    public boolean equals(Object o) {
        if(this == o) return true;
        if(o == null || getClass() != o.getClass()) return false;
        Vertex<?> vertex = (Vertex<?>) o;
        return dist == vertex.dist &&
                Objects.equals(val, vertex.val) &&
                Objects.equals(prev, vertex.prev) &&
                color == vertex.color;
    }

    @Override
    public int hashCode() {
        return Objects.hash(val, dist, prev, color);
    }

    @Override
    public String toString() {
        return val + "";
    }

}
