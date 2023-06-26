package ArrayBiSearch;

public class main {
    public static void main(String args[]) {
        Solution sol = new Solution();
        int[][] matrix;
        boolean finded;
        matrix = new int[][]{
                new int[]{1,3,5,7,9},
                new int[]{2,4,6,8,10},
                new int[]{11,13,15,17,19},
                new int[]{12,14,16,18,20},
                new int[]{21,22,23,24,25}
        };
        finded = sol.findNumberIn2DArray(matrix, 13);
        System.out.printf("find target %d from matrix: %b \n", 13, finded);
        matrix = new int[][]{
                new int[]{1, 4, 7, 11, 14, 17},
                new int[]{2, 5, 8, 12, 19, 22},
                new int[]{3, 6, 9, 16, 22, 25},
                new int[]{10, 13, 14, 17, 24, 29},
                new int[]{18, 21, 23, 26, 30, 32}
        };
        finded = sol.findNumberIn2DArray(matrix, 9);
        System.out.printf("find target %d from matrix: %b \n", 9, finded);
        finded = sol.findNumberIn2DArray(matrix, 11);
        System.out.printf("find target %d from matrix: %b \n", 11, finded);
        finded = sol.findNumberIn2DArray(matrix, 15);
        System.out.printf("find target %d from matrix: %b \n", 15, finded);
        return;
    }
}
