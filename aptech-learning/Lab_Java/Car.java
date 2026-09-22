import java.util.Arrays;
import java.util.List;

/**
 * Car.java
 * This enum defines the car brands available in the showroom,
 * including their prices, colors, and sales days.
 * 
 * Part of the Car Showroom Management System.
 * Author: Antigravity AI
 */
public enum Car {
    AUDI(
        Arrays.asList(5500, 3000, 4500),
        Arrays.asList(Color.WHITE, Color.YELLOW, Color.ORANGE),
        Arrays.asList(Day.FRIDAY, Day.SUNDAY, Day.MONDAY)
    ),
    MERCEDES(
        Arrays.asList(5000, 6000, 8500),
        Arrays.asList(Color.GREEN, Color.BLUE, Color.PURPLE),
        Arrays.asList(Day.TUESDAY, Day.SATURDAY, Day.WEDNESDAY)
    ),
    BMW(
        Arrays.asList(2500, 3000, 3500),
        Arrays.asList(Color.PINK, Color.RED, Color.BROWN),
        Arrays.asList(Day.MONDAY, Day.SUNDAY, Day.THURSDAY)
    );

    private final List<Integer> prices;
    private final List<Color> colors;
    private final List<Day> daySells;

    /**
     * Enum constructor to associate prices, colors, and sales days with each car brand.
     * 
     * @param prices list of prices corresponding to the colors
     * @param colors list of available colors
     * @param daySells list of days the car can be sold on
     */
    private Car(List<Integer> prices, List<Color> colors, List<Day> daySells) {
        this.prices = prices;
        this.colors = colors;
        this.daySells = daySells;
    }

    /**
     * Gets the list of prices for the car brand.
     * 
     * @return the list of prices
     */
    public List<Integer> getPrices() {
        return prices;
    }

    /**
     * Gets the list of available colors for the car brand.
     * 
     * @return the list of colors
     */
    public List<Color> getColors() {
        return colors;
    }

    /**
     * Gets the list of days the car brand is sold on.
     * 
     * @return the list of sales days
     */
    public List<Day> getDaySells() {
        return daySells;
    }

    /**
     * Parses the car brand string and returns the matching Car enum constant.
     * 
     * @param car the string representation of the car brand
     * @return the matching Car enum constant, or null if the string is invalid or null
     */
    public static Car getCar(String car) {
        if (car == null) {
            return null;
        }
        try {
            return Car.valueOf(car.trim().toUpperCase());
        } catch (IllegalArgumentException e) {
            return null;
        }
    }
}
