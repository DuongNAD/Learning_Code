package Day2;

public class ForEach {
    public static void main(String[] args) {
        int tong = 0;
        int[] a = {9,3,8,7,3,9,4,2};
        for(int x: a){
            if(x%2 ==0){
                tong = tong +x;
            }
        }
        System.out.println("Tong cac tren chia het cho 2: "+tong);
    }
}
