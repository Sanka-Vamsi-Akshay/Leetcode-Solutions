class Solution {
    public int maxDigitRange(int[] nums) {
        Map<Integer, Integer> s = new HashMap<>();
        int maxx, minn, tmp, r, gmax = 0;
        for(int num : nums){
            tmp = num;
            maxx = 0;
            minn = 9;
            while(tmp > 0){
                r = tmp % 10;
                if(r > maxx){
                    maxx = r;
                }
                if(r < minn){
                    minn = r;
                }
                tmp /= 10;
            }
            if((maxx - minn) > gmax){
                gmax = maxx - minn;
            }
            s.put(maxx - minn, s.getOrDefault((maxx - minn), 0) + num);
        }
        return s.get(gmax);
    }
}