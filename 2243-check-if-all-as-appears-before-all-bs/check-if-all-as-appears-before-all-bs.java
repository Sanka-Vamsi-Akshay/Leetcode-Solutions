class Solution {
    public boolean checkString(String s) {
        int n = s.length();
        int idx = 0;
        while (idx < n && s.charAt(idx) != 'b'){
            idx += 1;
        }
        while(idx < n){
            if(s.charAt(idx) == 'a'){
                return false;
            }
            idx += 1;
        }
        return true;
    }
}