class Solution {
    public int minMoves(int[] nums) {
        int maxx = 0;
        for(int num : nums){
            maxx = Math.max(maxx, num);
        }
        int res = 0;
        for(int num : nums){
            res += maxx - num;
        }
        return res;
    }
}