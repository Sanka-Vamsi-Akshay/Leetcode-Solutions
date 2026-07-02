class Solution {
    public int maxSubArray(int[] nums) {
        int tmp = nums[0];
        int res = nums[0];
        for(int i = 1; i < nums.length; i++){
            tmp = Math.max(nums[i], tmp + nums[i]);
            res = Math.max(res, tmp);
        }
        return res;
    }
}