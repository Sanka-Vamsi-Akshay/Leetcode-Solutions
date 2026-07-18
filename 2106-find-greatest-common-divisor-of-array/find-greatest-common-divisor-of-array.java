class Solution {
    public int GCD(int n1, int n2){
        if(n1 < n2){
            n1 = n1 + n2;
            n2 = n1 - n2;
            n1 = n1 - n2;
        }
        if(n1 % n2 == 0){
            return n2;
        }
        return GCD(n2, n1 % n2);
    }
    public int findGCD(int[] nums) {
        int maxx = nums[0];
        int minn = nums[0];
        for(int num : nums){
            if(num > maxx){
                maxx = num;
            }else if(num < minn){
                minn = num;
            }
        }
        return GCD(maxx, minn);
    }
}