class Solution {
    public int alternatingSum(int[] nums) {
        int sum = 0;
        boolean isEven = true;
        for(int i = 0; i < nums.length; i++){
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