class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int start = 0;
        int nbRows = matrix.length;
        int nbCols = matrix[0].length;
        int end = nbRows * nbCols - 1;
        int mid = 0;
        int row = 0;
        int col = 0;

        while (start <= end) {
            mid = (start+end)/2;
            row = mid / nbCols;
            col = mid % nbCols;

            if (target == matrix[row][col]) {
                return true;
            }
            if (target > matrix[row][col]) {
                if (start != mid) {
                    start = mid;
                }
                else {
                    start++;
                }
            }
            else {
                if (end != mid) {
                    end = mid;
                }
                else {
                    end--;
                }
            }
        }

        return false;
    }
}
