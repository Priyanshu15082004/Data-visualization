//package loop;
//print 1 to n
import java.util.Scanner;

public class Whileloop {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // int num = 1;
        // while(num <= n){
        //     System.out.println(num);
        //     num++;//incement operator ++, num = num +1
       //print sum and num
       int sum = 0;
       int num =1;
       while (num <= n) {
        
        sum = sum + num;
         num++;
       } 
        System.out.println(sum);
    }
    
}
