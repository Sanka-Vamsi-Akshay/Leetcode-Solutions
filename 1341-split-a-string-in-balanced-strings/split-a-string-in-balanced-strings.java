class Solution {
    public int balancedStringSplit(String s) {
        int tot = 0;
        int cnt = 0;
        for(char c : s.toCharArray()){
            tot += (c == 'R') ? 1 : -1;
            if(tot == 0){
                cnt += 1;
            }
        }
        return cnt;
    }
}