class Solution {
    public int countVowelStrings(int n) {
        int a = 1, e = 1, i = 1, o = 1, u = 1, tmp;
        for(int j = 0; j < n; j++){
            tmp = a + e + i + o + u;
            a = tmp - a;
            e = a - e;
            i = e - i;
            o = i - o;
            u = o;
            o = i;
            i = e;
            e = a;
            a = tmp;
        }
        return a;
    }
}