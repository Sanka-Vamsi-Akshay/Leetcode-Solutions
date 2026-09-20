class Solution {
    public int reverseDegree(String s) {
        int idx = 1, res = 0;
        for(char c : s.toCharArray()){
            res += ((123 - ((int) c)) * idx);
            idx += 1;
        }
        return res;
    }
}