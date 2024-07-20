//package operator;
import java.util.Scanner;

public class sumOfTwoNumber{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter first number");
        int num_1 = sc.nextInt();
        System.out.println("Enter second number");
        int num_2 = sc.nextInt();
        int sum = num_1 + num_2;
        System.out.println("sum:" +sum);
    }
}