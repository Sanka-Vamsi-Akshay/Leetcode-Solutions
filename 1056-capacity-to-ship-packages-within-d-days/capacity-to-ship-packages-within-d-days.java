class Solution {
    public boolean check(int[] weights, int days, int res){
        int tot = 0;
        for(int weight : weights){
            if(tot + weight > res){
                days -= 1;
                tot = weight;
            }else{
                tot += weight;
            }
        }
        return days > 0;
    }
    public int shipWithinDays(int[] weights, int days) {
        int l = 0;
        int r = 0;
        for(int weight : weights){
            l = Math.max(l, weight);
            r += weight;
        }
        int m;
        int res = 0;
        while(l <= r){
            m = l + ((r - l) / 2);
            if(check(weights, days, m)){
                res = m;
                r = m - 1;
            }else{
                l = m + 1;
            }
        }
        return res;
    }
}