import java.util.Arrays;
class Solution {
    public int minimumCost(int[] cost) {
        Arrays.sort(cost);
        int tot = 0;
        int l = cost.length;
        for(int i = 1; i < (l - (l % 3)); i++){
            if(i % 3 != 0){
                tot += cost[l - i];
            }
        }
        for(int i = 0; i < l % 3; i++){
            tot += cost[i];
        }
        return tot;
    }
}