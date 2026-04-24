class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> nbs = new Stack<>();

        for (int i = 0; i < tokens.length; i++) {
            if (tokens[i].compareTo("+") == 0) {
                nbs.push(nbs.pop() + nbs.pop());
            }
            else if (tokens[i].compareTo("*") == 0) {
                nbs.push(nbs.pop() * nbs.pop());
            }
            else if (tokens[i].compareTo("-") == 0) {
                int a = nbs.pop();
                nbs.push(nbs.pop() - a);
            }
            else if (tokens[i].compareTo("/") == 0) {
                int a = nbs.pop();
                nbs.push(nbs.pop() / a);
            }
            else {
                nbs.push(Integer.valueOf(tokens[i]));
            }
        }

        return nbs.peek();    
    }
}
