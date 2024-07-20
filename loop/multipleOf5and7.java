public class multipleOf5and7 {
    public static void main(String[] args) {
        //use break breakKeyword
        int num = 1;
        while(true){
            if((num % 5 ==0) && (num % 7==0)){
                System.out.println("Found ans" + num);
            break; 
            }
            num++;
        }
    }
    
}
