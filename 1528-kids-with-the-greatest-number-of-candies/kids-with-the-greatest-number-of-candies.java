import java.util.*;

class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int maxx = Integer.MIN_VALUE;
        for(int x : candies){
            if(x > maxx){
                maxx = x;
            }
        }
        List<Boolean> res = new ArrayList<>();
        for(int i : candies){
            res.add(i + extraCandies >= maxx);
        }
        return res;
    }
}