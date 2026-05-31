class Solution {
    public int digitFrequencyScore(int n) {
        int tot = 0;
        while(n > 0){
            tot += (n % 10);
            n /= 10;
        }
        return tot;
    }
}