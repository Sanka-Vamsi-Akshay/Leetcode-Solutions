class Solution {
    public int secondsBetweenTimes(String startTime, String endTime) {
        String[] startTimee = startTime.split(":");
        int h1 = Integer.parseInt(startTimee[0]);
        int m1 = Integer.parseInt(startTimee[1]);
        int s1 = Integer.parseInt(startTimee[2]);
        String[] endTimee = endTime.split(":");
        int h2 = Integer.parseInt(endTimee[0]);
        int m2 = Integer.parseInt(endTimee[1]);
        int s2 = Integer.parseInt(endTimee[2]);
        int res = 0;
        if(h1 == h2){
            if(m1 == m2){
                return s2 - s1;
            }else{
                res += ((m2 - m1 - 1) * 60);
                res += (60 - s1);
                res += s2;
                return res;
            }
        }else{
            res += (h2 - h1 - 1) * 3600;
            res += ((60 - m1 - 1) * 60);
            res += (60 - s1);
            res += (m2 * 60);
            res += s2;
            return res;
        }
    }
}