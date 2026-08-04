class Solution {
    public List<Integer> findMissingElements(int[] nums) {
        int minn = 101, maxx = 0;
        Set<Integer> s = new HashSet<>();
        for(int num : nums){
            if(num < minn){
                minn = num;
            }
            if(num > maxx){
                maxx = num;
            }
            s.add(num);
        }
        List<Integer> res = new ArrayList<>();
        for(int i = minn; i < maxx; i++){
            if(!s.contains(i)){
                res.add(i);
            }
        }
        return res;
    }
}