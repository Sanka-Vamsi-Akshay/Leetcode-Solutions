class Solution {
    public boolean judgeSquareSum(int c) {
        long l = 0;
        long r = (long)Math.ceil(Math.sqrt(c));
        long v;
        while(l <= r){
            v = (l * l) + (r * r);
            if(v > c){
                r -= 1;
            }else if(v < c){
                l += 1;
            }else{
                return true;
            }
        }
        return false;
    }
}