class Solution {
    public int[] leftRightDifference(int[] nums) {
        int tot = 0;
        for(int x : nums){
            tot += x;
        }
        int val = 0, lSum = 0, rSum = tot;
        for(int i = 0; i < nums.length; i++){
            val = nums[i];
            nums[i] = Math.abs(val + (2 * lSum) - tot);
            lSum += val;
        }
        return nums;
        
    }
}