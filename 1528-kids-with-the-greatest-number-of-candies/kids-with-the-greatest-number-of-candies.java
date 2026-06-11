import java.util.*;

class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int maxx = Integer.MIN_VALUE;
        int l = 0;
        for(int x : candies){
            if(x > maxx){
                maxx = x;
                l += 1;
            }
        }
        List<Boolean> res = new ArrayList<>();
        for(int i : candies){
            if(i + extraCandies >= maxx){
                res.add(true);
            }else{
                res.add(false);
            }
        }
        return res;
    }
}