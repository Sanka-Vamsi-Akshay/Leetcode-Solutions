import java.util.Map;
import java.util.HashMap;
class Solution {
    public int findMaxLength(int[] nums) {
        int res = 0;
        int tot = 0;
        Map<Integer, Integer> preSum = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            tot += (nums[i] == 0) ? -1 : 1;
            if(tot == 0){
                res = i + 1;
            }else{
                if(preSum.containsKey(tot)){
                    res = Math.max(res, i - preSum.get(tot));
                }else{
                    preSum.put(tot, i);
                }
            }
        }
        return res;
    }
}