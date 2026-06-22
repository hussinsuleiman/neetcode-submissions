class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<Integer> minStackIndices = new Stack<>();
        int[] result = new int[temperatures.length];

        for (int i = 0; i < temperatures.length; i++) {
            while (!minStackIndices.empty() && temperatures[minStackIndices.peek()] < temperatures[i]) {
                int index = minStackIndices.pop();
                result[index] = i - index;
            }
         
            minStackIndices.push(i);
        }

        return result;
    }
}
