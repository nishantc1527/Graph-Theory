package GraphTheory;

public class DirectedGraphAdjacencyMatrix implements GraphAdjacencyMatrix {

    public boolean[][] matrix;

    public DirectedGraphAdjacencyMatrix(int vertices) {
        matrix = new boolean[vertices][vertices];
    }

    @Override
    public void makeConnection(int val1, int val2, Integer... weight) {
        if(val1 < 0 || val2 < 0 || val1 >= matrix.length || val2 >= matrix.length) {
            throw new RuntimeException("Invalid Vertex");
        }

        matrix[val1][val2] = true;
    }

    @Override
    public boolean hasConnection(int val1, int val2) {
        if(val1 < 0 || val2 < 0 || val1 >= matrix.length || val2 >= matrix.length) {
            throw new RuntimeException("Invalid Vertex");
        }

        return matrix[val1][val2];
    }

    @Override
    public int weight(int val1, int val2) {
        return 0;
    }

}
