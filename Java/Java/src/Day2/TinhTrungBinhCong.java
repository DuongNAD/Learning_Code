package Day2;

public class TinhTrungBinhCong {
    public static void main(String[] args) {
        int sum = 0;
        for (int i = 27; i <= 250; i++) {
            if(i%3==0){
                sum = sum +i;
            }
        }
        System.out.println("Tong cac so tu 27 den 250 = " + sum);
    }
}
