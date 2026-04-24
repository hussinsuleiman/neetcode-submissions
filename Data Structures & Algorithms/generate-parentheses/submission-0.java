class Solution {
    private void backtrack(int open, int closed, int n, StringBuilder s, List<String> res) {
        if (open == closed && open == n) {
            res.add(s.toString());
            return;
        }

        if (open < n) {
            s.append('(');
            backtrack(open + 1, closed, n, s, res);
            s.deleteCharAt(s.length()-1);
        }

        if (closed < open) {
            s.append(')');
            backtrack(open, closed + 1, n, s, res);
            s.deleteCharAt(s.length()-1);
        }
    }

    public List<String> generateParenthesis(int n) {
        StringBuilder s = new StringBuilder();
        List<String> res = new ArrayList<>();
        backtrack(0, 0, n, s, res);
        return res;
    }
}
