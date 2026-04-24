class Solution {
    public int largestRectangleArea(int[] heights) {
        Stack<Integer> heightStack = new Stack<>();
        Stack<Integer> indexStack = new Stack<>();
        int maxArea = 0;
        int index = 0;

        for (int i = 0; i < heights.length; i++) {
            index = i;

            while (!heightStack.empty() && heights[i] < heightStack.peek()) {
                int height = heightStack.pop();
                index = indexStack.pop();
                maxArea = Math.max(maxArea, height * (i - index));
            }

            heightStack.push(heights[i]);
            indexStack.push(index);
        }

        while (!heightStack.empty()) {
            int height = heightStack.pop();
            index = indexStack.pop();
            maxArea = Math.max(maxArea, height * (heights.length - index));
        }

        return maxArea;
    }
}
