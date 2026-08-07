class Solution {
    public boolean isMiddleElementUnique(int[] nums) {
        int l = 0, r = nums.length - 1;
        int val = nums[r / 2];
        while(l < r){
            if(nums[l] == val || nums[r] == val){
                return false;
            }
            l += 1;
            r -= 1;
        }
        return true;
    }
}