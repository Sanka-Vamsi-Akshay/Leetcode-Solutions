class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        int n = nums.length;
        int tmp;
        for(int i = 0; i < n; i++){
            while((i + 1) != nums[i]){
                if(nums[nums[i] - 1] == nums[i]){
                    break;
                }
                tmp = nums[nums[i] - 1];
                nums[nums[i] - 1] = nums[i];
                nums[i] = tmp;
            }
        }
        List<Integer> res = new ArrayList<>();
        for(int i = 0; i < n; i++){
            if((i + 1) != nums[i]){
                res.add(nums[i]);
            }
        }
        return res;
    }
}