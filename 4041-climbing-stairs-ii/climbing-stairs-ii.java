class Solution {
    public int climbStairs(int n, int[] costs) {
        int m1 = 0, m2 = 0, m3 = 0, tmp;
        for(int c : costs){
            tmp = m3;
            m3 = Math.min(m1 + 9, Math.min(m2 + 4, tmp + 1)) + c;
            m1 = m2;
            m2 = tmp;
        }
        return m3;
    }
}