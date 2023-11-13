
import java.util.Scanner;

enum Command {
    ADD, LIST, SUM, QUIT, INVALID,
};

public class ArrayEnum {
    public static void main(String[] args) {
        final Scanner scanner = new Scanner(System.in);
        int[] values = new int[100];
        int index = 0;
        while (true) {
            final Command command = getCommand(scanner);
            if (command == Command.QUIT) {
                System.out.println("Bye!");
                break;
            }
            switch (command) {
                case ADD:
                    final int newValue = getValue(scanner);
                    values[index] = newValue;
                    index++;
                    break;
                case LIST:
                    printList(values, index);
                    break;
                case SUM:
                    System.out.println(getSum(values, index));
                    break;
                case INVALID:
                    System.out.println("Invalid Command");
                    break;
                default:
                    break;
            }
        }
        scanner.close();
    }

    private static Command getCommand(Scanner scanner) {
        String string_command_uppercase = scanner.next().toUpperCase();
        Command command;
        try{
            command = Command.valueOf(string_command_uppercase);
        }
        catch (IllegalArgumentException e){
            command = Command.INVALID;
        }
        return command;
    }

    private static int getValue(Scanner scanner) {
        int result = scanner.nextInt();
        return result;
    }

    private static void printList(int[] values, int index) {
        for (int i = 0; i < index; ++i) {
            System.out.print(values[i] + " ");
        }
        System.out.println();
    }

    private static int getSum(int[] values, int index) {
        int result = 0;
        for (int i = 0; i < index; ++i) {
            result += values[i];
        }
        return result;
    }
}
