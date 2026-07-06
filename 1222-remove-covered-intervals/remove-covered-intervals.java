class Solution {
    public int removeCoveredIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> {
            if (a[0] != b[0]){
                return Integer.compare(a[0], b[0]);
            }
            return Integer.compare(b[1], a[1]);
        });
        int[] last = new int[2];
        last[0] = intervals[0][0];
        last[1] = intervals[0][1];
        int cnt = 1;
        for(int[] curr : intervals){
            if(!(last[0] <= curr[0] && last[1] >= curr[1])){
                last[0] = curr[0];
                last[1] = curr[1];
                cnt += 1;
            }
        }
        return cnt;
    }
}