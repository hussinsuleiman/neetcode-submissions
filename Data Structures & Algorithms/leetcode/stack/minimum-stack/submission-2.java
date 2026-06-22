class MinStack {
    Stack<Integer> main;
    Stack<Integer> mins;

    public MinStack() {
        main = new Stack<>();
        mins = new Stack<>();    
    }
    
    public void push(int val) {
        main.push(val);
        if (mins.empty() || val <= mins.peek()) {
            mins.push(val);
        }
    }
    
    public void pop() {
        int top = main.pop();
        if (top == mins.peek()) {
            mins.pop();
        }
    }
    
    public int top() {
        return main.peek();
    }
    
    public int getMin() {
        return mins.peek();
    }
}
