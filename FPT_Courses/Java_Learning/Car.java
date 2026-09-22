public class Car {
    // Attributes (Thuộc tính)
    private String maker;
    private int price;

    // Default Constructor (Hàm khởi tạo mặc định)
    public Car() {
    }

    // Parameterized Constructor (Hàm khởi tạo có tham số)
    public Car(String maker, int price) {
        this.maker = maker;
        this.price = price;
    }

    // Getter for maker with Title Case logic
    public String getMaker() {
        if (maker == null || maker.isEmpty()) {
            return maker;
        }

        String[] words = maker.split("\\s+"); // Split by whitespace
        StringBuilder titleCaseMaker = new StringBuilder();

        for (String word : words) {
            if (!word.isEmpty()) {
                // Capitalize the first letter, append the rest
                String capitalized = word.substring(0, 1).toUpperCase() + word.substring(1).toLowerCase();
                titleCaseMaker.append(capitalized).append(" ");
            }
        }
        return titleCaseMaker.toString().trim();
    }

    public void setMaker(String maker) {
        this.maker = maker;
    }

    public int getPrice() {
        return price;
    }

    // Added this method explicitly to allow subclasses to modify price
    public void setPrice(int price) {
        this.price = price;
    }

    @Override
    public String toString() {
        // Format: maker, price [cite: 8]
        return maker + ", " + price;
    }
}