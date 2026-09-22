/**
 * Day.java
 * This enum defines the days of the week and provides utility methods
 * for parsing day values from user inputs.
 * 
 * Part of the Car Showroom Management System.
 * Author: Antigravity AI
 */
public enum Day {
    MONDAY,
    TUESDAY,
    WEDNESDAY,
    THURSDAY,
    FRIDAY,
    SATURDAY,
    SUNDAY;

    /**
     * Parses the day string and returns the matching Day enum constant.
     * 
     * @param day the string representation of the day
     * @return the matching Day enum constant, or null if the string is invalid or null
     */
    public static Day getDay(String day) {
        if (day == null) {
            return null;
        }
        try {
            return Day.valueOf(day.trim().toUpperCase());
        } catch (IllegalArgumentException e) {
            return null;
        }
    }
}
