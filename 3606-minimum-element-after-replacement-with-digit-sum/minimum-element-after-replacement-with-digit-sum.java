class Solution {
    public int minElement(int[] nums) {
        int minn = 10001;
        int tot;
        for(int x : nums){
            tot = 0;
            while(x > 0){
                tot += (x % 10);
                x /= 10;
            }
            if(tot < minn){
                minn = tot;
            }
        }
        return minn;
    }
}