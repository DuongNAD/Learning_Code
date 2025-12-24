package Day5;

import java.sql.SQLOutput;

public class ChuNhat {
    double dai,rong;

    public ChuNhat(){

    }

    public ChuNhat(double dai,double rong){
        this.dai=dai;
        this.rong=rong;
    }

    public ChuNhat(double dai){
        this.dai=dai;
    }



    public static void main(String[] args) {
        ChuNhat chuNhat = new ChuNhat();
        System.out.println(chuNhat.dai);
        System.out.println(chuNhat.rong);

        ChuNhat chuNhat2 = new ChuNhat(10,20);
        System.out.println(chuNhat2.dai);
        System.out.println(chuNhat2.rong);

        ChuNhat chuNhat3 = new ChuNhat(300);
        System.out.println(chuNhat3.dai);
    }
}
