class Solution {
    public int alternatingSum(int[] nums) {
        int sum = 0;
        boolean isEven = true;
        for(int num : nums){
            if(isEven){
                sum += num;
            }else{
                sum -= num;
            }
            isEven = !isEven;
        }
        return sum;
    }
}