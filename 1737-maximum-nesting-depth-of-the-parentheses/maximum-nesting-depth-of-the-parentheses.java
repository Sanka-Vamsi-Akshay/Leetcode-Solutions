class Solution {
    public int maxDepth(String s) {
        int res = 0, curr = 0;
        for(char c : s.toCharArray()){
            if(c == '('){
                curr += 1;
            }else if(c == ')'){
                res = Math.max(res, curr);
                curr -= 1;
            }
        }
        return res;
    }
}