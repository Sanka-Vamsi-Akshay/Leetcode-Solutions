class Solution {
    public int numOfSubarrays(int[] arr) {
        int evenCnt = 1, oddCnt = 0, tot = 0, res = 0, mod = 1000000007;
        for(int num : arr){
            tot += num;
            if(tot % 2 == 0){
                evenCnt += 1;
                res += oddCnt;
                evenCnt %= mod;
            }else{
                oddCnt += 1;
                res += evenCnt;
                oddCnt %= mod;
            }
            res %= mod;
        }
        return res;
    }
}