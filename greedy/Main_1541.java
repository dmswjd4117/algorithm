import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main_1541 {
    public static void main(String[] args) throws FileNotFoundException {
        System.setIn(new java.io.FileInputStream("data.txt"));

		Scanner sc = new Scanner(System.in);
 
        StringTokenizer arr = new StringTokenizer(sc.nextLine(), "-");
        int answer = 0;
        boolean flag = false;
        while(arr.hasMoreTokens()){
            int temp = 0;
            StringTokenizer add_arr = new StringTokenizer(arr.nextToken(), "+");
            while(add_arr.hasMoreTokens()){
                temp += Integer.parseInt(add_arr.nextToken());
            }
            if(!flag){
                answer = temp;
                flag = true;
            }else{
                answer -= temp;
            }
        }

        System.out.println(answer);
        sc.close();
    }
}
