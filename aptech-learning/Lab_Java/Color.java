/**
 * Color.java
 * This enum defines the available car colors in the showroom,
 * including a special NO_COLOR option representing an unpainted car.
 * 
 * Part of the Car Showroom Management System.
 * Author: Antigravity AI
 */
public enum Color {
    WHITE,
    YELLOW,
    ORANGE,
    GREEN,
    BLUE,
    PURPLE,
    PINK,
    RED,
    BROWN,
    NO_COLOR;

    /**
     * Parses the color string and returns the matching Color enum constant.
     * 
     * @param color the string representation of the color
     * @return the matching Color enum constant, or null if the string is invalid or null
     */
    public static Color getColor(String color) {
        if (color == null) {
            return null;
        }
        try {
            return Color.valueOf(color.trim().toUpperCase());
        } catch (IllegalArgumentException e) {
            return null;
        }
    }
}
