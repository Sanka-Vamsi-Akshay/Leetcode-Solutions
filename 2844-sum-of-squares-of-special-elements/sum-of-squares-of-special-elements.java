class Solution {
    public int sumOfSquares(int[] nums) {
        int n = nums.length;
        int res = 0;
        for(int i = 1; i <= Math.floor(Math.sqrt(n)); i++){
            if(n % i == 0){
                res += Math.pow(nums[i - 1], 2);
                if(n != i * i){
                    res += Math.pow(nums[(n / i) - 1], 2);
                }
            }
        }
        return res;
    }
}