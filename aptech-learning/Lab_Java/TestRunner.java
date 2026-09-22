/**
 * TestRunner.java
 * Automated test harness to verify the correctness of the Car Showroom Management System.
 * Tests all requirements, edge cases, standard validations, and exception messages.
 * 
 * Author: Antigravity AI
 */
public class TestRunner {

    private static int testsRun = 0;
    private static int testsPassed = 0;

    public static void main(String[] args) {
        System.out.println("=== STARTING CAR SHOWROOM SYSTEM AUTOMATED TESTS ===\n");

        // Test Case 1: Wrong brand name (returns null) -> Expects "Car break"
        runTest(
            "TC01: Wrong Brand Name",
            Car.getCar("AUDI123"),
            Color.getColor("WHITE"),
            Day.getDay("FRIDAY"),
            "5500",
            "Can't sell Car: Car break"
        );

        // Test Case 2: Price contains letters -> Expects "Price is digit"
        runTest(
            "TC02: Price with Letters",
            Car.getCar("AUDI"),
            Color.getColor("WHITE"),
            Day.getDay("FRIDAY"),
            "5500a",
            "Can't sell Car: Price is digit"
        );

        // Test Case 3: Price contains special characters -> Expects "Price is digit"
        runTest(
            "TC03: Price with Special Characters",
            Car.getCar("AUDI"),
            Color.getColor("WHITE"),
            Day.getDay("FRIDAY"),
            "$5500",
            "Can't sell Car: Price is digit"
        );

        // Test Case 4: Price is negative -> Expects "Price greater than zero"
        runTest(
            "TC04: Negative Price",
            Car.getCar("AUDI"),
            Color.getColor("WHITE"),
            Day.getDay("FRIDAY"),
            "-5500",
            "Can't sell Car: Price greater than zero"
        );

        // Test Case 5: Price is zero -> Expects "Price greater than zero"
        runTest(
            "TC05: Zero Price",
            Car.getCar("AUDI"),
            Color.getColor("WHITE"),
            Day.getDay("FRIDAY"),
            "0",
            "Can't sell Car: Price greater than zero"
        );

        // Test Case 6: Wrong Day name (returns null) -> Expects "Car can't sell today"
        runTest(
            "TC06: Wrong Day Name",
            Car.getCar("AUDI"),
            Color.getColor("WHITE"),
            Day.getDay("FRIDAYY"),
            "5500",
            "Can't sell Car: Car can't sell today"
        );

        // Test Case 7: Brand not sold on that day -> Expects "Car can't sell today"
        runTest(
            "TC07: Brand Not Sold On Day (MERCEDES on MONDAY)",
            Car.getCar("MERCEDES"),
            Color.getColor("BLUE"),
            Day.getDay("MONDAY"),
            "6000",
            "Can't sell Car: Car can't sell today"
        );

        // Test Case 8: Wrong Color name (returns null) -> Expects "color car does not exist"
        runTest(
            "TC08: Wrong Color Name",
            Car.getCar("AUDI"),
            Color.getColor("WHITEE"),
            Day.getDay("FRIDAY"),
            "5500",
            "Can't sell Car: color car does not exist"
        );

        // Test Case 9: Color not available for brand (BMW PINK is valid, but not for AUDI) -> Expects "color car does not exist"
        runTest(
            "TC09: Color Not Available for Brand (AUDI has no PINK)",
            Car.getCar("AUDI"),
            Color.getColor("PINK"),
            Day.getDay("FRIDAY"),
            "5500",
            "Can't sell Car: color car does not exist"
        );

        // Test Case 10: Insufficient funds for colored car -> Expects "Price is less than..."
        runTest(
            "TC10: Insufficient Funds (WHITE AUDI is $5500, customer pays $5000)",
            Car.getCar("AUDI"),
            Color.getColor("WHITE"),
            Day.getDay("FRIDAY"),
            "5000",
            "Can't sell Car: Price is less than the actual price of the colored car ($5500)"
        );

        // Test Case 11: Valid sale (WHITE AUDI, $5500, FRIDAY) -> Expects Success (no exception)
        runTest(
            "TC11: Valid Colored Car Sale",
            Car.getCar("AUDI"),
            Color.getColor("WHITE"),
            Day.getDay("FRIDAY"),
            "5500",
            null
        );

        // Test Case 12: Valid sale with NO_COLOR discount (YELLOW AUDI listed is $3000, unpainted is $2900, customer pays $2900) -> Expects Success
        runTest(
            "TC12: Valid Unpainted Car Sale (NO_COLOR, paying $2900)",
            Car.getCar("AUDI"),
            Color.getColor("NO_COLOR"),
            Day.getDay("FRIDAY"),
            "2900",
            null
        );

        // Test Case 13: Invalid sale with NO_COLOR due to too low budget (YELLOW AUDI unpainted is $2900, customer pays $2800) -> Expects "Price is less than..."
        runTest(
            "TC13: Insufficient Funds for Unpainted Car (NO_COLOR, paying $2800)",
            Car.getCar("AUDI"),
            Color.getColor("NO_COLOR"),
            Day.getDay("FRIDAY"),
            "2800",
            "Can't sell Car: Price is less than the actual price of the unpainted car (minimum $2900)"
        );

        System.out.println("\n=== TEST RESULTS SUMMARY ===");
        System.out.println("Tests Run: " + testsRun);
        System.out.println("Tests Passed: " + testsPassed);
        System.out.println("Tests Failed: " + (testsRun - testsPassed));
        if (testsPassed == testsRun) {
            System.out.println("\nALL TESTS PASSED SUCCESSFULLY! The system is 100% compliant and robust.");
        } else {
            System.out.println("\nSOME TESTS FAILED! Please inspect the logs above.");
        }
    }

    private static void runTest(String testName, Car car, Color color, Day day, String price, String expectedError) {
        testsRun++;
        try {
            CarValidation.checkCar(car, color, day, price);
            if (expectedError != null) {
                System.out.println("[FAIL] " + testName + " -> Expected exception: \"" + expectedError + "\" but execution succeeded.");
            } else {
                System.out.println("[PASS] " + testName + " -> Succeeded as expected.");
                testsPassed++;
            }
        } catch (ExceptionCar e) {
            if (expectedError == null) {
                System.out.println("[FAIL] " + testName + " -> Expected success but threw: \"" + e.getMessage() + "\"");
            } else if (e.getMessage().equals(expectedError)) {
                System.out.println("[PASS] " + testName + " -> Correctly threw: \"" + e.getMessage() + "\"");
                testsPassed++;
            } else {
                System.out.println("[FAIL] " + testName + " -> Expected exception: \"" + expectedError + "\" but got: \"" + e.getMessage() + "\"");
            }
        }
    }
}
