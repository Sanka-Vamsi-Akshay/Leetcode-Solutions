class Solution {
    public boolean checkDivisibility(int n) {
        int s = 0, p = 1, tmp = n, r;
        while(tmp > 0){
            r = tmp % 10;
            s += r;
            p *= r;
            tmp /= 10;
        }
        return n % (s + p) == 0;
    }
}