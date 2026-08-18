class Solution {
    public int largestInteger(int[] nums, int k) {
        int n = nums.length;
        if(k == n){
            int res = 0;
            for(int num : nums){
                res = Math.max(res, num);
            }
            return res;
        }
        if(n == 1){
            return nums[0];
        }
        if(k == 1){
            int t = n - 1;
            Arrays.sort(nums);
            for(int i = n - 1; i >= 0; i--){
                if(nums[i] != nums[t]){
                    if(i + 1 == t){
                        return nums[t];
                    }
                    else{
                        t = i;
                    }
                }
            }
            if(nums[0] != nums[1]){
                return nums[0];
            }
            return -1;
        }
        if(nums[0] == nums[n - 1]){
            return -1;
        }
        int n1 = nums[0], n2 = nums[n - 1], l = 1;
        boolean f1 = true, f2 = true;
        while(l <= (n - l - 1)){
            if(f1){
                if(nums[l] == n1 || nums[n - l - 1] == n1){
                    f1 = false;
                }
            }
            if(f2){
                if(nums[l] == n2 || nums[n - l - 1] == n2){
                    f2 = false;
                }
            }
            if(!f1 && !f2){
                return -1;
            }
            l++;
        }
        if(f1 && f2){
            return Math.max(n1, n2);
        }else if(f1){
            return n1;
        }else{
            return n2;
        }
    }
}