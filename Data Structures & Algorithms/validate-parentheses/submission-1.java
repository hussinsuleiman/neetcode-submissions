class Solution {
    public boolean isValid(String s) {
        Stack<Character> par = new Stack<Character>();

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '[' || s.charAt(i) == '(' || s.charAt(i) == '{') {
                par.push(s.charAt(i));
            }
            else if (s.charAt(i) == ']') {
                if (par.empty() || par.peek() != '[') {
                    return false;
                }
                par.pop();
            }
            else if (s.charAt(i) == ')') {
                if (par.empty() || par.peek() != '(') {
                    return false;
                }
                par.pop();
            }
            else if (s.charAt(i) == '}') {
                if (par.empty() || par.peek() != '{') {
                    return false;
                }
                par.pop();
            }
        }

        return par.empty();
    }
}
