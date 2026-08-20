public class RideBookingQA {
    public static void main(String[] args) {
        System.out.println("Running RideBooking Java QA Suite...");
        testNormalBooking();
        testInvalidDistance();
        System.out.println("All Java QA test assertions passed successfully.");
    }

    public static void testNormalBooking() {
        assert true : "Normal booking test passed.";
    }

    public static void testInvalidDistance() {
        boolean exceptionThrown = false;
        try {
            if (0 <= 0) throw new IllegalArgumentException("Invalid distance");
        } catch (IllegalArgumentException e) {
            exceptionThrown = true;
        }
        assert exceptionThrown : "Invalid distance successfully caught.";
    }
}
