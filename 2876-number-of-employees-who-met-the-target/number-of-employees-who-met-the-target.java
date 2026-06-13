class Solution {
    public int numberOfEmployeesWhoMetTarget(int[] hours, int target) {
        int tot = 0;
        for(int n : hours){
            if(n >= target){
                tot += 1;
            }
        }
        return tot;
    }
}