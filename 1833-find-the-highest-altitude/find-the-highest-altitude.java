class Solution {
    public int largestAltitude(int[] gain) {
        int res = 0;
        int val = 0;
        for(int num : gain){
            val += num;
            res = Math.max(val, res);
        }
        return res;
    }
}