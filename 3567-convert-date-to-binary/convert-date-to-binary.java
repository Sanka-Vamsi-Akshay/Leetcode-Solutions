import java.util.Arrays;
class Solution {
    public String toBin(String n){
        int num = Integer.parseInt(n);
        long res = 0;
        int p = 0;
        while(num > 0){
            if(num % 2 == 1){
                res += Math.pow(10, p);
            }
            num /= 2;
            p += 1;
        }
        return Long.toString(res);
    }
    public String convertDateToBinary(String date) {
        String[] arr = date.split("-");
        arr[0] = toBin(arr[0]);
        arr[1] = toBin(arr[1]);
        arr[2] = toBin(arr[2]);
        return arr[0] + "-" + arr[1] + "-" + arr[2];
    }
}