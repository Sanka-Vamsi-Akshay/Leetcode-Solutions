class Solution {
    public int[] transformArray(int[] nums) {
        int i = 0;
        int tmp;
        for(int j = 0; j < nums.length; j++){
            nums[j] %= 2;
            if(nums[j] == 0){
                tmp = nums[i];
                nums[i] = nums[j];
                nums[j] = tmp;
                i += 1;
            }
        }
        return nums;
        
    }
}