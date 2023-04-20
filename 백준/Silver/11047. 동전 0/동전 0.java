import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        long money = Integer.parseInt(st.nextToken());
        int[] A = new int[N];
        for(int i=0;i<N;i++){
            A[i] = Integer.parseInt(br.readLine());
        }
        int cnt =0;
        for(int i=N-1;i>=0;i--){
            if(money/A[i] > 0) {
                cnt += money / A[i];
                money = money % A[i];
            }
        }
        System.out.println(cnt);
    }
}

