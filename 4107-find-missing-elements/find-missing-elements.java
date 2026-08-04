class Solution {
    public List<Integer> findMissingElements(int[] nums) {
        int minn = nums[0];
        int maxx = nums[0];
        Set<Integer> s = new HashSet<>();
        for(int num : nums){
            minn = Math.min(minn, num);
            maxx = Math.max(maxx, num);
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