import java.util.Map;
import java.util.HashMap;
class Solution {
    public int numIdenticalPairs(int[] nums) {
        int[] freq = new int[101];
        for(int n : nums){
            freq[n] += 1;
        }
        int tot = 0;
        for(int n : freq){
            tot += ((n * (n - 1)) / 2);
        }
        return tot;
    }
}