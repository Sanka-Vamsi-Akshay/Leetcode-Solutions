class Solution {
    public int longestMonotonicSubarray(int[] nums) {
        int res = 1, tot = 1, i = 1, n = nums.length;
        while(i < n){
            tot = 1;
            while(i < n && nums[i - 1] < nums[i]){
                i++;
                tot++;
            }
            res = Math.max(res, tot);
            tot = 1;
            while(i < n && nums[i - 1] > nums[i]){
                i++;
                tot++;
            }
            res = Math.max(res, tot);
            while(i < n && nums[i - 1] == nums[i]){
                i++;
            }
        }
        return res;
    }
}