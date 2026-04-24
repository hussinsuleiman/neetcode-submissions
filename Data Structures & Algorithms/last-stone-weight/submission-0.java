class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> stoneWeights = new PriorityQueue<>();

        for (int i = 0; i < stones.length; i++) {
            stoneWeights.offer(-stones[i]);
        }

        while (stoneWeights.size() > 1) {
            stoneWeights.offer(stoneWeights.poll() - stoneWeights.poll());
        }
        
        return -stoneWeights.poll();
    }
}
