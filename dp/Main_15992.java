package dp;

import java.util.HashMap;
import java.util.Scanner;
import java.util.Map.Entry;

public class Main_15992 {
    static Scanner kb = new Scanner(System.in);
    static long dp[][] = new long[1002][1002];
    static final long mod = 1000000009L;
    public static void main(String[] args) {
      int T = kb.nextInt();
      dp[1][1] = 1;
      
      dp[2][1] = 1;
      dp[2][2] = 1;

      dp[3][1] = 1;
      dp[3][2] = 2;
      dp[3][3] = 1;
      

      for(int i=4; i<= 1000; i++){
        for(int j=1; j<=1000; j++){
          dp[i][j] = (dp[i-1][j-1] + dp[i-2][j-1] + dp[i-3][j-1] )% mod; 
        }
      }

      for(int test=0; test<T; test++){
        int a = kb.nextInt();
        int b = kb.nextInt();
        System.out.println(dp[a][b] % mod);
      }
    }
}