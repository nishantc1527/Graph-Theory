package GraphTheory;

public class WeightedGraphAdjacencyMatrix implements GraphAdjacencyMatrix {

    public int[][] matrix;

    public WeightedGraphAdjacencyMatrix(int vertices) {
        matrix = new int[vertices][vertices];
    }

    @Override
    public void makeConnection(int val1, int val2, Integer... weight) {
        if(val1 < 0 || val2 < 0 || val1 >= matrix.length || val2 >= matrix.length) {
            throw new RuntimeException("Invalid Vertex");
        }

        matrix[val1][val2] = weight[0];
    }

    @Override
    public boolean hasConnection(int val1, int val2) {
        if(val1 < 0 || val2 < 0 || val1 >= matrix.length || val2 >= matrix.length) {
            throw new RuntimeException("Invalid Vertex");
        }

        return matrix[val1][val2] != 0;
    }

    @Override
    public int weight(int val1, int val2) {
        if(val1 < 0 || val2 < 0 || val1 >= matrix.length || val2 >= matrix.length) {
            throw new RuntimeException("Invalid Vertex");
        }

        return matrix[val1][val2];
    }

}
