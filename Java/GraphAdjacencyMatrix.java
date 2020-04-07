package GraphTheory;

public interface GraphAdjacencyMatrix {

    void makeConnection(int val1, int val2, Integer... weight);
    boolean hasConnection(int val1, int val2);
    int weight(int val1, int val2);

}
