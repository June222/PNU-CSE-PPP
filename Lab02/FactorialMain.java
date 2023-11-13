package Lab02;

public class FactorialMain {
    public static void main(String[] args) {

        for (int i = 1; i <= 10; i++) {
            // String leftSideString = "1";

            // for (int j = 2; j <= i; j++) {
            // leftSideString += "*" + String.valueOf(j);
            // }

            System.out.println("Factorial of " + i + ": " + factorial(i));
        }
    }

    private static long factorial(final int n) {
        long result = 1;

        if (n <= 1) {
            result = n;
        }

        else {
            for (int i = 1; i <= n; i++) {
                result *= i;
            }
        }

        return result;
    }
}