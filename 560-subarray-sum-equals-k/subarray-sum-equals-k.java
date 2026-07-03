import java.util.Map;
import java.util.HashMap;
class Solution {
    public int subarraySum(int[] nums, int k) {
        int summ = 0;
        int res = 0;
        int diff;
        Map<Integer, Integer> preSum = new HashMap<>();
        preSum.put(0, 1);
        for(int num : nums){
            summ += num;
            diff = summ - k;
            res += preSum.getOrDefault(diff, 0);
            preSum.put(summ, preSum.getOrDefault(summ, 0) + 1);
        }
        return res;
    }
}