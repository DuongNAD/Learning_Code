package JavaClassDay3;

public class Goat {
    private String name;
    private int weight;

    public Goat(){

    }

    public Goat(String name, int weight) {
        this.name = name;
        this.weight = weight;
    }
    public String getName() {
        return this.name + "_" + this.weight;
    }
    public void setName(String name) {
        this.name = name;
    }
    public int getWeight() {
        return weight;
    }
    public void setWeight(int newWeight) {
        int oldWeight = this.weight;
        int n =0;

        if(oldWeight == 0){
            n =1;
        }
        else {
            int temp = Math.abs(oldWeight);
            while(temp >0){
                int digit = temp % 10;
                if(digit % 2 == 0){
                    n++;
                }
                temp /= 10;
            }
        }

        this.weight = newWeight*n;
    }
    @Override
    public String toString() {
        return "Goat{" + "name=" + name + ", weight=" + weight + '}';
    }
}
