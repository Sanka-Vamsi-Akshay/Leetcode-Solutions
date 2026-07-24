class Solution {
    public boolean canReach(int[] start, int[] target) {
        if((start[0] % 2) == (target[0] % 2)){
            return (start[1] % 2) == (target[1] % 2);
        }
        return (start[1] % 2) != (target[1] % 2);
    }
}