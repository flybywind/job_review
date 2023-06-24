package ArrayBiSearch;

public class Solution {
    int nRow, nCol;
    int[][] matrix;

    int[] binarySearchAxis(int axis, int idx, int start, int end, int elem) {
        if (axis == 0) {
            // search along first axis: row
            if (this.matrix[idx][start] > elem) {
                return new int[]{start - 1, start};
            }
            if (this.matrix[idx][end - 1] < elem) {
                return new int[]{end, end + 1};
            }
            int mid = (start + end) / 2;
            int midV = this.matrix[idx][mid];
            if (start == end - 1) {
                if (this.matrix[idx][start] == elem) {
                    // found
                    return new int[]{start, start};
                } else {
                    // not found
                    return new int[]{start, end};
                }
            }
            if (midV > elem) {
                return binarySearchAxis(axis, idx, start, mid, elem);
            } else if (midV < elem) {
                return binarySearchAxis(axis, idx, mid + 1, end, elem);
            } else {
                return new int[]{mid, mid};
            }
        } else {
            // search along second axis: row
            if (this.matrix[start][idx] > elem) {
                return new int[]{start - 1, start};
            }
            if (this.matrix[end - 1][idx] < elem) {
                return new int[]{end, end + 1};
            }
            int mid = (start + end) / 2;
            int midV = this.matrix[mid][idx];
            if (start == end - 1) {
                if (this.matrix[start][idx] == elem) {
                    // found
                    return new int[]{start, start};
                } else {
                    // not found
                    return new int[]{start, end};
                }
            }
            if (midV > elem) {
                return binarySearchAxis(axis, idx, start, mid, elem);
            } else if (midV < elem) {
                return binarySearchAxis(axis, idx, mid + 1, end, elem);
            } else {
                return new int[]{mid, mid};
            }
        }
    }

    boolean findNumberIn2DArray(int target, int rowStart, int rowEnd, int colStart, int colEnd) {
        if (target < matrix[rowStart][colStart]) {
            return false;
        }
        if (target > matrix[rowEnd - 1][colEnd - 1]) {
            return false;
        }
        if (rowEnd - rowStart == 1) {
            int[] res = binarySearchAxis(0, rowStart, colStart, colEnd, target);
            return res[0] == res[1];
        }
        if (colEnd - colStart == 1) {
            int[] res = binarySearchAxis(1, colStart, rowStart, rowEnd, target);
            return res[0] == res[1];
        }
        if (rowEnd - rowStart < colEnd - colStart) {
            int[] rowRes0 = binarySearchAxis(0, rowStart, colStart, colEnd, target);
            int[] rowRes1 = binarySearchAxis(0, rowEnd - 1, colStart, colEnd, target);
            if (rowRes0[0] == rowRes0[1] || rowRes1[0] == rowRes1[1]) {
                return true;
            }
            int colStart1 = rowRes1[1], colEnd1 = rowRes0[0];
            if (colStart1 >= this.nCol || colEnd1 < 0) {
                return false;
            }
            return findNumberIn2DArray(target, rowStart + 1, rowEnd - 1, colStart1, colEnd1);
        } else {
            int[] colRes0 = binarySearchAxis(1, colStart, rowStart, rowEnd, target);
            int[] colRes1 = binarySearchAxis(1, colEnd - 1, rowStart, rowEnd, target);
            if (colRes0[0] == colRes0[1] || colRes1[0] == colRes1[1]) {
                return true;
            }
            int rowStart1 = colRes1[1], rowEnd1 = colRes0[0];
            if (rowStart1 >= this.nRow || rowEnd1 < 0) {
                return false;
            }
            return findNumberIn2DArray(target, rowStart1, rowEnd1, colStart + 1, colEnd - 1);
        }
    }

    public boolean findNumberIn2DArray(int[][] matrix, int target) {
        if (matrix == null) {
            return false;
        }
        this.matrix = matrix;
        this.nRow = matrix.length;
        if (this.nRow == 0) {
            return false;
        }
        this.nCol = matrix[0].length;
        return findNumberIn2DArray(target, 0, nRow, 0, nCol);
    }
}