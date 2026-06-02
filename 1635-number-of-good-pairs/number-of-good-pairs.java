import java.util.Map;
import java.util.HashMap;
class Solution {
    public int numIdenticalPairs(int[] nums) {
        Map<Integer, Integer> freq = new HashMap<>();
        for(int n : nums){
            if(freq.containsKey(n)){
                freq.put(n, freq.get(n) + 1);
            }else{
                freq.put(n, 1);
            }
        }
        int tot = 0;
        for(int v : freq.values()){
            tot += ((v * (v - 1)) / 2);
        }
        return tot;
    }
}