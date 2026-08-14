import java.util.Map;
import java.util.HashMap;
class Solution {
    public int maximumLengthSubstring(String s) {
        Map<Character, Integer> freq = new HashMap<>();
        int l = 0, r = 0, res = 0;
        for(char c : s.toCharArray()){
            freq.put(c, freq.getOrDefault(c, 0) + 1);
            while(freq.get(c) > 2){
                freq.put(s.charAt(l), freq.get(s.charAt(l)) - 1);
                l += 1;
            }
            res = Math.max(res, r - l + 1);
            r += 1;
        }
        return res;
    }
}