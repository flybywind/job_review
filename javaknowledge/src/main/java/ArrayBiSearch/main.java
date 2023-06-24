package ArrayBiSearch;

public class main {
  static int[] binarySearchAxis(int[][] matric, int axis, int idx, int start, int end, int elem) {
    if (axis == 1) {
      // search along first axis: column
      int mid = (start+end)/2;
      int midV = matric[idx][mid];
      if (start == end-1) {
        if (matric[idx][start] == elem) {
          // found
          return new int[] {start, start};
        } else {
          // not found
          return new int[] {start, end};
        }
      }
      if (midV > elem) {
        return binarySearchAxis(matric, axis, idx, start, mid, elem);
      } else if (midV < elem) {
        return binarySearchAxis(matric, axis, idx, mid+1, end, elem);
      } else {
        return new int[]{mid, mid};
      }
    } else {
      // search along second axis: row
      int mid = (start+end)/2;
      int midV = matric[mid][idx];
      if (start == end-1) {
        if (matric[start][idx] == elem) {
          // found
          return new int[]{start, start};
        } else {
          // not found
          return new int[]{start, end};
        }
      }
      if (midV > elem) {
        return binarySearchAxis(matric, axis, idx, start, mid, elem);
      } else if (midV < elem) {
        return binarySearchAxis(matric, axis,  idx,mid+1, end, elem);
      } else {
        return new int[]{mid, mid};
      }
    }
  }
  static  boolean _findNumberIn2DArray(int [][]matrix, int target, int rowStart, int rowEnd, int colStart, int colEnd) {
    if (target < matrix[colStart][rowStart]) {
      return false;
    }
    if (target > matrix[colEnd-1][rowEnd-1]) {
      return false;
    }
    if (rowEnd - rowStart == 1) {
      int[] res = binarySearchAxis(matrix, 1, rowStart, colStart, colEnd, target);
      return res[0] == res[1];
    }
    if (colEnd - colStart == 1) {
      int[] res = binarySearchAxis(matrix, 0, colStart, rowStart, rowEnd, target);
      return res[0] == res[1];
    }
    if (rowEnd - rowStart < colEnd - colStart) {
      int[] rowRes0 = binarySearchAxis(matrix, 1, rowStart, colStart, colEnd, target);
      int[] rowRes1 = binarySearchAxis(matrix, 1, rowEnd-1, colStart, colEnd, target);
      if (rowRes0[0] == rowRes0[1] || rowRes1[0] == rowRes1[1]) {
        return true;
      }
      int rowStart1 = rowRes1[1], rowEnd1 = rowRes0[0];
      return _findNumberIn2DArray(matrix, target, rowStart1, rowEnd1, colStart, colEnd);
    } else {
      int[] colRes0 = binarySearchAxis(matrix, 0, colStart, rowStart, rowEnd, target);
      int[] colRes1 = binarySearchAxis(matrix, 0, colEnd-1, rowStart, rowEnd, target);
      if (colRes0[0] == colRes0[1] || colRes1[0] == colRes1[1]) {
        return true;
      }
      int colStart1 = colRes1[1], colEnd1 = colRes0[0];
      return _findNumberIn2DArray(matrix, target, rowStart, rowEnd, colStart1, colEnd1);
    }
  }
  public static boolean findNumberIn2DArray(int[][] matrix, int target) {
    if (matrix == null) {
      return false;
    }
    int nRow = matrix.length;
    if (nRow == 0) {
      return false;
    }
    int nCol = matrix[0].length;
    return _findNumberIn2DArray(matrix, target, 0, nRow, 0, nCol);
  }

  public static void main(String args[]){
    int[][] matrix = new int[][]{
        new int[]{1, 4, 7, 11, 14, 17},
        new int[]{2, 5, 8, 12, 19, 22},
        new int[]{3, 6, 9, 16, 22, 25},
        new int[]{10, 13, 14, 17, 24, 29},
        new int[] {18, 21, 23, 26, 30, 32}
    } ;
    boolean finded = findNumberIn2DArray(matrix, 9);
    System.out.printf("find target %d from matrix: %b \n", 9, finded);
    finded = findNumberIn2DArray(matrix, 11);
    System.out.printf("find target %d from matrix: %b \n", 11, finded);
    finded = findNumberIn2DArray(matrix, 15);
    System.out.printf("find target %d from matrix: %b \n", 15, finded);
    return;
  }
}