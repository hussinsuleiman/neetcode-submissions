class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int i = 0;
        int j = numbers.length-1;
        int[] output = new int[2]; 

        while (i < j && numbers[i] + numbers[j] != target) {
            if (numbers[i] + numbers[j] < target) {
                i++;
            }
            else {
                j--;
            }
        }

        output[0] = i+1;
        output[1] = j+1;

        return output;
    }
}
