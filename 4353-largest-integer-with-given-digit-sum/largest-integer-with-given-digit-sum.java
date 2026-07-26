class Solution {
    public int largestInteger(int n, int s) {
        if(s > (9 * n)){
            return -1;
        }
        int res = 0;
        while(s > 8){
            res = (res * 10) + 9;
            s -= 9;
            n -= 1;
        }
        if(n > 0){
            res = (res * 10) + s;
            n -= 1;
        }
        for(int i = 0; i < n; i++){
            res = res * 10;
        }
        return res;
    }
}