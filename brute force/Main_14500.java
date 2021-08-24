// https://www.acmicpc.net/problem/14500


import java.io.FileNotFoundException;
import java.util.*;


public class Main_14500 {
    static int n, m;
    static int ans;
    static int arr[][];
    static boolean vis[][];
    static ArrayList<Point> points = new ArrayList<>();

    static int exp[][][] =  {
            {{0, 0}, {-1, 0}, {0, -1}, {0, 1}},
            {{0, 0}, {-1, 0}, {1, 0}, {0, 1}},
            {{0, 0}, {0, -1}, {0, 1},{1, 0}},
            {{0, 0}, {0, -1}, {-1, 0}, {1, 0}}
    };

    static int moving[][] = {
            {0, 1}, {1, 0}, {0, -1}, {-1, 0}
    } ;

    static class Point {
        int x, y;
        public Point (int x, int y){
            this.x = x;
            this.y = y;
        }
    }


    public static void main(String[] args) throws FileNotFoundException {
        System.setIn(new java.io.FileInputStream("data.txt"));
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        m = sc.nextInt();

        arr = new int[n][m];
        vis = new boolean[n][m];

        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                arr[i][j] = sc.nextInt();
            }
        }


        for(int i=0; i<n; i++){
            for(int j=0; j<m ; j++){
                vis[i][j] = true;
                find(i, j, 0, 0);
                vis[i][j] = false;

            }
        }

        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                ex_find(i, j);
            }
        }

        System.out.println(ans);

        sc.close();
    }

    static public boolean isin(int x, int y){
        if(x >= 0 && y >= 0 && x < n && y < m){
            return true;
        }
        return false;
    }

    public static void ex_find(int x,int y){

        for(int rotate=0; rotate<exp.length; rotate++){
            int hap = 0;
            boolean flag = true;

            for(int i=0; i<4; i++){
                int nx = x + exp[rotate][i][0];
                int ny = y + exp[rotate][i][1];
                if(!isin(nx, ny)){
                    flag = false;
                    break;
                }

                hap += arr[nx][ny];
            }


            if(flag && hap > ans) {
                ans = hap;
            }
        }
    }

    static void find(int x, int y, int cnt, int hap){

        if(cnt == 4){
            if(ans < hap){
                ans = hap;
            }
            return;
        }


        for(int i=0; i<4; i++){
            int nx = x + moving[i][0];
            int ny = y + moving[i][1];
            if(! isin(nx, ny)){
                continue;
            }
            if(vis[nx][ny]){
                continue;
            }
            vis[nx][ny] = true;
            find(nx, ny, cnt+1, hap+arr[nx][ny]);
            vis[nx][ny] = false;
        }
    }

}
