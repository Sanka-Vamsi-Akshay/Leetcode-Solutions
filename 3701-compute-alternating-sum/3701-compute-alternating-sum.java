class Solution {
    public int alternatingSum(int[] nums) {
        int sum = 0;
        boolean isEven = true;
        int l = nums.length;
        for(int i = 0; i < l; i++){
            if(isEven){
                sum += nums[i];
            }else{
                sum -= nums[i];
            }
            isEven = !isEven;
        }
        return sum;
    }
}