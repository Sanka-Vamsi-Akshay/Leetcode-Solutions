class Solution {
    public int minMoves(int[] nums) {
        int maxx = 0;
        int tot = 0;
        for(int num : nums){
            maxx = Math.max(maxx, num);
            tot += num;
        }
        return (nums.length * maxx) - tot;
    }
}