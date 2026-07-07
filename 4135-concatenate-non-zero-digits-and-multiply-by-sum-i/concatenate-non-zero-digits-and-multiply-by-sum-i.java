class Solution {
    public long sumAndMultiply(int n) {
        int sum = 0;
        int x = 0;
        int val;
        int p = 1;
        while(n > 0){
            val = n % 10;
            if(val != 0){
                sum += val;
                x += (p * val);
                p *= 10;
            }
            n /= 10;
        }
        return (long) x * sum;
    }
}