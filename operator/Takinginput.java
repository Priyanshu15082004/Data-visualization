package operator;
import java.util.Scanner;

public class Takinginput {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter your name");
        // String name = sc.next();
        //This is for full line output nextline()
        String name = sc.nextLine();
        System.out.println("Name is: " +name);

        // System.out.println("Enter your Lucky number");
        // int num_1 = sc.nextInt();
        // System.out.println("Lucky Numbr is:" + num_1);
    }
}
