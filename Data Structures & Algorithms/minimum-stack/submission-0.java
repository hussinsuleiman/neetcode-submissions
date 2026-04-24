class MinStack {
    Stack<Integer> s;
    Stack<Integer> mins;

    public MinStack() {
        this.s = new Stack<Integer>();
        this.mins = new Stack<Integer>();   
    }
    
    public void push(int val) {
        if (mins.empty() || val <= mins.peek()) {
            mins.push(val);
        }

        s.push(val);
    }
    
    public void pop() {
        int a = s.pop();

        if (a == mins.peek()) {
            mins.pop();
        }
    }
    
    public int top() {
        return s.peek();
    }
    
    public int getMin() {
        return mins.peek();
    }
}
