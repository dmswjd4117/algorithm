import java.io.FileNotFoundException;
import java.util.Scanner;

// import java.util.stream.IntStream;

public class Main_2138 {
    static int INF=987654321;
    static int n, answer=INF;
    static int[] a, b, copy;

    public static void print(int arr[]){
        for(int a: arr){
            System.out.print(a+" ");
        }
        System.out.println();
    }


    public static void flip(int[] a, int index){
        int n = a.length;
        for(int i=index-1; i<=index+1; i++){
            if(i >= 0 && i<n){
                a[i] = 1 - a[i];
            }
        }
    }

    public static boolean check(int[] arr, int[] ans){
        for(int i=0; i<arr.length; i++){
            if(arr[i] != ans[i]){
                return false;
            }
        }
        return true;
    }

    public static boolean right_differ(int[] arr, int index){
        if(arr[index+1] != b[index+1]){
            return true;
        }
        return false;
    }

    public static void go(int arr[], int index, int cnt){
        if(check(arr, b)){
            answer = Math.min(cnt, answer);
            return;
        }
        if(index == -1){
            return;
        }

        if(right_differ(arr, index)){
            flip(arr, index);
            go(arr, index-1, cnt+1);
        }else{
            go(arr, index-1, cnt);
        }


    }

    public static void main(String[] args) throws FileNotFoundException {
        System.setIn(new java.io.FileInputStream("data.txt"));

        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        a = new int[n];
        b = new int[n];
        copy = new int[n];

        String string = sc.next();
        for(int i=0; i<n; i++){
            a[i] = string.charAt(i) - '0';
            copy[i] = a[i];
        }
        string = sc.next();
        for(int i=0; i<n; i++){
            b[i] = string.charAt(i) - '0';
        }

//        0번째 flip x
        go(copy, n-2, 0);

//        0번째 flip o
        for(int i=0; i<n; i++){
            copy[i] = a[i];
        }
        flip(copy, n-1);
        go(copy, n-2, 1);

        if(answer != INF){
            System.out.println(answer);
        }else{
            System.out.println(-1);
        }

        sc.close();
    }
}
