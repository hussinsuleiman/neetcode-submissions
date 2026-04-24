class KthLargest {
    PriorityQueue<Integer> largestK;
    int k;

    public KthLargest(int k, int[] nums) {
        this.largestK = new PriorityQueue<>();
        this.k = k;

        for (int i = 0; i < Math.min(k, nums.length); i++) {
            this.largestK.offer(nums[i]);
        }
        for (int i = k; i < nums.length; i++) {
            this.largestK.offer(nums[i]);
            this.largestK.poll();
        }
    }
    
    public int add(int val) {
        this.largestK.offer(val);
        if (this.largestK.size() > this.k) {
            this.largestK.poll();
        }
        return this.largestK.peek();
    }
}
