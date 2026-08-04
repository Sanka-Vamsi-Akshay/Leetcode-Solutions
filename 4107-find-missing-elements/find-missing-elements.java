class Solution {
    public List<Integer> findMissingElements(int[] nums) {
        int minn = nums[0];
        int maxx = nums[0];
        for(int num : nums){
            minn = Math.min(minn, num);
            maxx = Math.max(maxx, num);
        }
        int[] arr = new int[maxx + 1];
        for(int num : nums){
            arr[num]++;
        }
        List<Integer> res = new ArrayList<>();
        for(int i = minn; i < maxx; i++){
            if(arr[i] == 0){
                res.add(i);
            }
        }
        return res;
    }
}