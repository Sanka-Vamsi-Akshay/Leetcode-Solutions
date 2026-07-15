class Solution {
    /*public int GCD(int n1, int n2){
        if(n1 > n2){
            n1 = n1 + n2;
            n2 = n1 - n2;
            n1 = n1 - n2;
        }
        if((n2 % n1) == 0){
            return n1;
        }
        return GCD(n2 % n1, n1);
    }*/
    public int gcdOfOddEvenSums(int n) {
        /*int evenSum = n * (n + 1);
        int oddSum = evenSum - n;
        return GCD(oddSum, evenSum);*/
        return n;
    }
}