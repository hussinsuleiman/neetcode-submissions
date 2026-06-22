class Solution {
    public boolean isOp(String s) {
        return (s.compareTo("+") == 0 || s.compareTo("-") == 0 || s.compareTo("*") == 0 || s.compareTo("/") == 0);
    }

    public int evalRPN(String[] tokens) {
        Stack<Integer> nbs = new Stack<>();
        
        for (int i = 0; i < tokens.length; i++) {
            if (isOp(tokens[i])) {
                int a = nbs.pop();
                int b = nbs.pop();

                if (tokens[i].compareTo("+") == 0) {
                    nbs.push(a + b);
                }
                else if (tokens[i].compareTo("-") == 0) {
                    nbs.push(b - a);
                }
                else if (tokens[i].compareTo("*") == 0) {
                    nbs.push(a * b);
                }
                else {
                    nbs.push(b / a);
                }
            }
            else {
                nbs.push(Integer.valueOf(tokens[i]));
            }
        }

        return nbs.peek();
    }
}
