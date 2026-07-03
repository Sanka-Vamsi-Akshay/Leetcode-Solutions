import java.util.Arrays;
class Solution {
    public int maximumGap(int[] nums) {
        Arrays.sort(nums);
        int val = nums[0];
        int res = 0;
        for(int num : nums){
            res = Math.max(res, num - val);
            val = num;
        }
        return res;
    }
}