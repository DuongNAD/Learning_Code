package Day6;

public class B1 {
    public static void main(String[] args) {
        int[] array = new int[]{5,6,7,8};
        m(array);
        System.out.println(array[0]);
    }
    public static void m(int[] x){
        x[0] +=5;
        System.out.println(x[0]);
    }
}
