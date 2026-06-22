import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;

class plantsVSbadguys {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.valueOf(br.readLine());
        String[] ints = br.readLine().split(" ");
        int[] Ri = new int[N];
        
        for (int i = 0; i < N; i++) {
            Ri[i] = Integer.valueOf(ints[i]); 
        }
        
        int minimum = Ri[0];
        
        for (int i = 1; i < N; i++) {
            if (Ri[i] < minimum) {
                minimum = Ri[i];
            }
        }
        
        System.out.println(minimum+1);
    } 
}
