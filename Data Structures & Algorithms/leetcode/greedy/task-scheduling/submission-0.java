class Solution {
    public int leastInterval(char[] tasks, int n) {
        HashMap<Character, Integer> occChar = new HashMap<>();
        PriorityQueue<Integer> freq = new PriorityQueue<>();
        Queue<int[]> wait = new LinkedList<>();

        int time = 0;

        for (int i = 0; i < tasks.length; i++) {
            occChar.put(tasks[i], occChar.getOrDefault(tasks[i], 0)+1);
        }

        for (Character c : occChar.keySet()) {
            freq.add(-occChar.get(c));
        }

        while (!freq.isEmpty() || !wait.isEmpty()) {
            time++;

            if (!freq.isEmpty()) {
                int count = freq.poll() + 1;

                if (count < 0) {
                    wait.add(new int[] {count, time + n});
                }
            }
            
            if (!wait.isEmpty() && wait.peek()[1] == time) {
                freq.add(wait.poll()[0]);
            }
        }

        return time;
    }
}
