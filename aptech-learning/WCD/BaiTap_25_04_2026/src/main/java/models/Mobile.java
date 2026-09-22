package models;

public class Mobile {
    private int id;
    private String name;
    private double price;
    private String warranty;
    private String accessories;
    private boolean inOutStock;
    private String image;

    public Mobile() {}

    public Mobile(int id, String name, double price, String warranty, String accessories, boolean inOutStock, String image) {
        this.id = id;
        this.name = name;
        this.price = price;
        this.warranty = warranty;
        this.accessories = accessories;
        this.inOutStock = inOutStock;
        this.image = image;
    }

    public Mobile(String name, double price, String warranty, String accessories, boolean inOutStock, String image) {
        this.name = name;
        this.price = price;
        this.warranty = warranty;
        this.accessories = accessories;
        this.inOutStock = inOutStock;
        this.image = image;
    }

    // Getters and Setters
    public int getId() { return id; }
    public void setId(int id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public double getPrice() { return price; }
    public void setPrice(double price) { this.price = price; }
    public String getWarranty() { return warranty; }
    public void setWarranty(String warranty) { this.warranty = warranty; }
    public String getAccessories() { return accessories; }
    public void setAccessories(String accessories) { this.accessories = accessories; }
    public boolean isInOutStock() { return inOutStock; }
    public void setInOutStock(boolean inOutStock) { this.inOutStock = inOutStock; }
    public String getImage() { return image; }
    public void setImage(String image) { this.image = image; }
}
