class Solution {
    public boolean threeFibonacciSum(int n) {
        int tot = 2;
        int a = 1;
        int b = 1;
        int tmp;
        while(tot < n){
            tot += (2 * a);
            tmp = a + b;
            a = b;
            b = tmp;
        }
        return tot == n;
    }
}