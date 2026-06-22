import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Arrays;

class sortOfSorting {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.valueOf(br.readLine());
        StringBuilder output = new StringBuilder();
        HashMap<Integer, String> names_codes = new HashMap();

        while (N != 0) {
            if (!output.isEmpty()) {
                output.append("\n");
                output.append("\n");
            }

            String[] names = new String[N];
            int[] codes = new int[N];
            for (int i = 0; i < N; i++) {
                names[i] = br.readLine();
                codes[i] = (200 * N) * names[i].charAt(0) + (2 * N) * names[i].charAt(1) + i;
                names_codes.put(codes[i], names[i]);
            }

            Arrays.sort(codes);

            output.append(names_codes.get(codes[0]));
            for (int i = 1; i < N; i++) {
                output.append("\n");
                output.append(names_codes.get(codes[i]));
            }

            N = Integer.valueOf(br.readLine());
        }

        System.out.println(output);
    }
}