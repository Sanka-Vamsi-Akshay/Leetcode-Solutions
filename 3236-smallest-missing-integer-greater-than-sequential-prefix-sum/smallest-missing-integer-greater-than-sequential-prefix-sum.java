import java.util.Set;
import java.util.HashSet;
class Solution {
    public int missingInteger(int[] nums) {
        int val = nums[0], tot = 0;
        for(int num : nums){
            if(num != val){
                break;
            }
            tot += val;
            val += 1;
        }
        Set<Integer> s = new HashSet<>();
        for(int i = val - nums[0] - 1; i < nums.length; i++){
            s.add(nums[i]);
        }
        while(s.contains(tot)){
            tot += 1;
        }
        return tot;
    }
}