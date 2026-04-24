class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        HashMap<Integer, Integer> positionToSpeed = new HashMap<>();
        Stack<Float> times = new Stack<>();

        for (int i = 0; i < position.length; i++) {
            positionToSpeed.put(position[i], speed[i]);
        }

        Arrays.sort(position);

        for (int i = position.length-1; i >= 0; i--) {
            int speedCar = positionToSpeed.get(position[i]);
            float time = ( (float) (target) - position[i])/speedCar;
            
            if (times.empty() || times.peek() < time) {
                times.push(time);
            }
        }

        return times.size();
    }
}
