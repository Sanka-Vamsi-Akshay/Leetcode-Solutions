class Solution {
    public long sumAndMultiply(int n) {
        int sum = 0;
        int x = 0;
        int val;
        int p = 0;
        while(n > 0){
            val = n % 10;
            if(val != 0){
                sum += val;
                x += (Math.pow(10, p) * val);
                p += 1;
            }
            n /= 10;
        }
        return (long) x * sum;
    }
}