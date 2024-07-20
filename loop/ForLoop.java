import java.util.Scanner;
//Print the sum of the n natural number 
public class ForLoop {
    public static void main(String[] args) {
        Scanner sc =new Scanner(System.in);
     int n = sc.nextInt();
    //  for(int num = 1; num <= n; num++){
    //     System. .println(num);
    //print sum and num
    int sum = 0;
    for(int num =1; num<= n; num++){
sum = sum + num;

    }
System.out.println("sum of numbers upto n: " + sum);
    }
}
