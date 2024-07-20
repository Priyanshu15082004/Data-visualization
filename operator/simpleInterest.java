package operator;
import java.util.Scanner;

public class simpleInterest {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter principle");
        float p = sc.nextFloat();
        System.out.println("enter rate of interest");
        float r = sc.nextFloat();
        System.out.println("Enter time");
        float t = sc.nextFloat();
        float si = (p * r * t)/100;
        System.out.println("principle: " + p);
        System.out.println("Rate: " + r);
        System.out.println("Time: " + t);
        System.out.println("Simple Interest" + si);

    }

    
}
