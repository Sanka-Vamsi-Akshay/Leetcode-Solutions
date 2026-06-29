class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0;
        int right = numbers.length - 1;
        int tot;
        int[] res = new int[2];
        while(left < right){
            tot = numbers[left] + numbers[right];
            if(tot > target){
                right -= 1;
            }else if(tot < target){
                left += 1;
            }else{
                res[0] = left + 1;
                res[1] = right + 1;
                break;
            }
        }
        return res;
    }
}