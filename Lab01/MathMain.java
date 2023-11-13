package Lab01;
import java.util.Scanner;

public class MathMain {
    public static void main(String[] args){

        System.out.println("Enter two numbers: ");

        final Scanner scanner = new Scanner(System.in);

        final int begin = scanner.nextInt();
        final int end = scanner.nextInt();

        scanner.close();

        final long sum = getSumBetween(begin, end);

        System.out.printf("Sum between %d and %d : %,d%n", begin, end, sum);
        // printSumBetween(begin, end ,sum);

        final long product = getProductBetween(begin, end);

        System.out.printf("Product between %d and %d : %,d%n", begin, end, product);
        // printProductBetween(begin, end, product);
    }

    private static long getSumBetween(final int begin, final int end){
        long result = 0;

        for(int i = begin; i <= end; i++){
            result += i;
        }

        return result;
    }
    private static void printSumBetween(final int begin, final int end, final long sum){
        String leftSide = String.valueOf(begin);

        for(int i = begin + 1; i <= end ; i++){
            leftSide += "+" + String.valueOf(i);
        }

        System.out.printf("%s = %,d\n",leftSide,sum);
    }
    private static long getProductBetween(final int begin, final int end){
        long result = 1;

        for(int i = begin; i <= end; i++){
            result *= i;
        }

        return result;
    }
    private static void printProductBetween(final int begin, final int end, final long product){
        String leftSide = String.valueOf(begin);

        for(int i = begin + 1; i <= end; i++){
            leftSide += "*" + String.valueOf(i);
        }

        System.out.printf("%s = %,d\n",leftSide,product);    
    }
}
