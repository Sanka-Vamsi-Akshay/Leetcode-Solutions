class Solution {
    public boolean canAliceWin(int n) {
        int ch = 10;
        boolean res = false;
        while(n >= ch){
            n -= ch;
            ch -= 1;
            res = !res;
        }
        return res;
    }
}