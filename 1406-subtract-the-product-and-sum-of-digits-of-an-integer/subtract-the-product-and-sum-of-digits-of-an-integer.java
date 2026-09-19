class Solution {
    public int subtractProductAndSum(int n) {
        int prod = 1, sum = 0, tmp;
        while(n > 0){
            tmp = n % 10;
            n /= 10;
            prod *= tmp;
            sum += tmp;
        }
        return prod - sum;
    }
}