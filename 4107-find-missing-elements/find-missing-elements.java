class Solution {
    public List<Integer> findMissingElements(int[] nums) {
        Arrays.sort(nums);
        int tmp = nums[0];
        List<Integer> res = new ArrayList<>();
        for(int num : nums){
            while(num != tmp){
                res.add(tmp);
                tmp += 1;
            }
            tmp += 1;
        }
        return res;
    }
}