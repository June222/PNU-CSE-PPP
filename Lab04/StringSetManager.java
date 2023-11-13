// package Lab04;

// package Lab04;
import java.util.Scanner;

enum StringCommand { ADD, REMOVE, CLEAN, QUIT, INVALID}

public class StringSetManager {
    public static void main(String[] args) {

        final Scanner scanner = new Scanner(System.in);
        String[] stringSet = new String[100];

        while ( true ) {
            final StringCommand command = getCommand(scanner);
            if ( command == StringCommand.QUIT ) {
                System.out.println("BYE!"); break;
            }
            switch ( command ) {
                case ADD: {
                    final String str = getString(scanner);
                    executeAdd(stringSet, str);
                    break;
                }
                case REMOVE: {
                    final String str = getString(scanner);
                    executeRemove(stringSet, str);
                    break;
                }
                case CLEAN: {
                    executeClear(stringSet);
                    break;
                }
                default:
                    System.out.println("Unknown Command!");
                    break;
            }
            executePrint(stringSet);
        }
    }

    private static void executePrint(String[] stringSet) {
        int size = 0;
        for (String s : stringSet) {
            if(s!=null)
                size++;
            else
                break;
        }
        System.out.print("Element Size: " + size);
        System.out.print(", Values = ");
        for (int i = 0; i < size; i++) {
            if (i != 0) {
                System.out.print(", ");
            }
            System.out.print(stringSet[i]);
        }
        System.out.println();
    }

    private static void executeClear(String[] stringSet) {
        for (int i = 0; i < 100; i++) {
            if (stringSet[i]==null)
                break;
            stringSet[i] = null;
        }
    }

    private static void executeRemove(String[] stringSet, String str) {
        for (int i = 0; i < 100; i++) {
            if (stringSet[i] == null)
                break;
            if (str.equals(stringSet[i])){
                for (int j = i; j < 99; j++) {
                    if (stringSet[j]==null){
                        break;
                    }
                    stringSet[j] = stringSet[j+1];
                }
            }
        }
    }

    private static void executeAdd(String[] stringSet, String str) {
        if (str.equals("Good")){
            for (int i = 0; i < 100; i++) {
                if (stringSet[i]==null){
                    for (int j = i; j > 0; j--) {
                        stringSet[j] = stringSet[j-1];
                    }
                    break;
                }
            }
            stringSet[0]=str;
        }

        else{
            for (int i = 0; i < 100; ++i) {
                if(stringSet[i] == null){
                    stringSet[i] = str;
                    break;
                }
                if (str.equals(stringSet[i]))
                    break;
            }
        }
    }
    // Your code here

    private static String getString(Scanner scanner) {
        return scanner.next();
    }

    private static StringCommand getCommand(Scanner scanner) {
        String str_cmd = scanner.next().toUpperCase();
        StringCommand cmd;
        try{
            cmd = StringCommand.valueOf(str_cmd);
        }catch(IllegalArgumentException e){
            cmd = StringCommand.INVALID;
        }
        return cmd;
    }
    // Your code here
}
