import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Arrays;

class Cocktail {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] ints = br.readLine().split(" ");
        int N = Integer.valueOf(ints[0]);
        int T = Integer.valueOf(ints[1]);
        int[] times = new int[N];
        boolean possible = true;
        
        for (int i = 0; i < N; i++) {
            times[i] = Integer.valueOf(br.readLine());
        }
        
        Arrays.sort(times);
        
        for (int i = N-1; i >= 0; i--) {
            if (times[i] <= i*T) {
                System.out.println("NO");
                possible = false;
                break;
            }
        }
        
        if (possible) {
            System.out.println("YES");
        }
    }
}