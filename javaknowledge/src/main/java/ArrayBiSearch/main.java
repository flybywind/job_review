package ArrayBiSearch;

import javax.swing.plaf.SliderUI;

public class main {
    public static void main(String args[]) {
        int[][] matrix = new int[][]{
                new int[]{1, 4, 7, 11, 14, 17},
                new int[]{2, 5, 8, 12, 19, 22},
                new int[]{3, 6, 9, 16, 22, 25},
                new int[]{10, 13, 14, 17, 24, 29},
                new int[]{18, 21, 23, 26, 30, 32}
        };
        Solution sol = new Solution();
        boolean finded = sol.findNumberIn2DArray(matrix, 9);
        System.out.printf("find target %d from matrix: %b \n", 9, finded);
        finded = sol.findNumberIn2DArray(matrix, 11);
        System.out.printf("find target %d from matrix: %b \n", 11, finded);
        finded = sol.findNumberIn2DArray(matrix, 15);
        System.out.printf("find target %d from matrix: %b \n", 15, finded);
        return;
    }
}
