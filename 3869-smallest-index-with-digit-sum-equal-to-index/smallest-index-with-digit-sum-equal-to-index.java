class Solution {
    public int smallestIndex(int[] nums) {
        int tmp, tot;
        for(int i = 0; i < nums.length; i++){
            tot = 0;
            tmp = nums[i];
            while(tmp > 0){
                tot += (tmp % 10);
                tmp /= 10;
            }
            if(tot == i){
                return i;
            }
        }
        return -1;
    }
}