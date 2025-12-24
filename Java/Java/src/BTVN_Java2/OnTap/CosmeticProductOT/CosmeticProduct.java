package BTVN_Java2.OnTap.CosmeticProductOT;

import java.io.Serializable;

public class CosmeticProduct implements Serializable, Comparable<CosmeticProduct> {
    private int productID;
    private String productName;
    private double productPrice;

    public CosmeticProduct(int productID, String productName, double productPrice) {
        this.productID = productID;
        this.productName = productName;
        this.productPrice = productPrice;
    }
    public int getProductID() {
        return productID;
    }
    public void setProductID(int productID) {
        this.productID = productID;
    }
    public String getProductName() {
        return productName;
    }
    public void setProductName(String productName) {
        this.productName = productName;
    }
    public double getProductPrice() {
        return productPrice;
    }
    public void setProductPrice(double productPrice) {
        this.productPrice = productPrice;
    }
    @Override
    public String toString() {
        return ("Product ID: " + this.productID + " - " + " Product Name: " + this.productName + " - " + " Product Price: " + this.productPrice);
    }

    @Override
    public int compareTo(CosmeticProduct other){
        return Double.compare(this.productPrice, other.productPrice);
    }

}
