class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        int[][] res = new int[r][c];
        int m = mat.length;
        int n = mat[0].length;
        if((m * n) != (r * c)){
            return mat;
        }
        int row = 0;
        int col = 0;
        for(int i = 0; i < m; i++){
            for(int num : mat[i]){
                res[row][col] = num;
                col += 1;
                if(col == c){
                    col = 0;
                    row += 1;
                }
            }
        }
        return res;
    }
}