package dp; 

import java.util.Scanner;

public class Main_9465 {
    static Scanner kb = new Scanner(System.in);
    public static void main(String[] args) {
        int test = Integer.parseInt(kb.nextLine());

        for(int T = 0; T < test; T++){
            int N = Integer.parseInt(kb.nextLine());
  
            int[][] arr = new int[2][N];
            int[][] d = new int[2][N];

            for(int i=0; i<2; i++){
                String[] str = kb.nextLine().split(" ");
            
                for(int j=0; j<N; j++){
                    arr[i][j] = Integer.parseInt(str[j]);
                }
            }

            d[0][0] = arr[0][0];
            d[1][0] = arr[1][0];

            for(int j=1; j<N; j++){
                for(int i=0 ; i<=1; i++){
                    d[i][j] = Math.max(d[1-i][j-1]+arr[i][j], d[i][j-1]);
                }
            }

            System.out.println(Math.max(d[0][N-1], d[1][N-1]));
        }
    }    
}