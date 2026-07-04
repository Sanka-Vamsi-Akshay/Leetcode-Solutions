class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length;
        int n = nums2.length;
        int idx1 = 0;
        int idx2 = 0;
        int val;
        if((m + n) % 2 == 0){
            val = ((m + n) / 2) - 1;
        }else{
            val = (m + n) / 2;
        }
        for(int i = 0; i < val; i++){
            if(idx1 < m && idx2 < n){
                if(nums1[idx1] < nums2[idx2]){
                    idx1 += 1;
                }else{
                    idx2 += 1;
                }
            }else if(idx1 < m){
                idx1 += 1;
            }else{
                idx2 += 1;
            }
        }
        double tot = 0;
        val = ((m + n) % 2 == 0) ? 2 : 1;
        for(int i = 0; i < val; i++){
            if(idx1 < m && idx2 < n){
                if(nums1[idx1] < nums2[idx2]){
                    tot += nums1[idx1];
                    idx1 += 1;
                }else{
                    tot += nums2[idx2];
                    idx2 += 1;
                }
            }else if(idx1 < m){
                tot += nums1[idx1];
                idx1 += 1;
            }else{
                tot += nums2[idx2];
                idx2 += 1;
            }
        }
        return (val == 1) ? tot : tot / 2;
    }
}