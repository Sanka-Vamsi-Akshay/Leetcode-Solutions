class Solution {
    public double findMaxAverage(int[] nums, int k) {
        long res = 0;
        for(int i = 0; i < k; i++){
            res += nums[i];
        }
        long tmp = res;
        for(int i = k; i < nums.length; i++){
            tmp = tmp + nums[i] - nums[i - k];
            if(tmp > res){
                res = tmp;
            }
        }
        float x = k;
        return (double)res / x;
    }
}