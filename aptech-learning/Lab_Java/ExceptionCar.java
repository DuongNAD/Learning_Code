/**
 * ExceptionCar.java
 * Custom exception class for the Car Showroom Management System.
 * Inherits from the default Exception class in Java and is used to report
 * validation errors during a vehicle sale check.
 * 
 * Part of the Car Showroom Management System.
 * Author: Antigravity AI
 */
public class ExceptionCar extends Exception {
    
    /**
     * Constructs a new ExceptionCar with the specified detail message.
     * 
     * @param message the detail error message
     */
    public ExceptionCar(String message) {
        super(message);
    }
}
