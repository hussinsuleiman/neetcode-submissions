class Solution {
    public boolean isValid(String s) {
        Stack<Character> parentheses = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            char letter = s.charAt(i);

            if (letter == '(' || letter == '{' || letter == '[') {
                parentheses.push(letter);
            }
            else if (parentheses.empty()) {
                return false;
            }
            else {
                char top = parentheses.peek();
                if (top == '(' && letter != ')' || top == '{' && letter != '}' || top == '[' && letter != ']') {
                    return false;
                }
                else {
                    parentheses.pop();
                }
            }
        }

        return parentheses.empty(); 
    }
}
