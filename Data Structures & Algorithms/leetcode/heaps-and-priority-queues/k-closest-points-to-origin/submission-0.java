class Solution {
    public int[][] kClosest(int[][] points, int k) {
        HashMap<Double, ArrayList<int[]>> distToPt = new HashMap<>(); 
        PriorityQueue<Double> kSmallestDist = new PriorityQueue<>();

        for (int i = 0; i < Math.min(points.length, k); i++) {
            double dist = Math.sqrt(points[i][0] * points[i][0] + points[i][1] * points[i][1]);
            if (!distToPt.containsKey(-dist)) {
                distToPt.put(-dist, new ArrayList<int[]>());
            }
            distToPt.get(-dist).add(points[i]);
            kSmallestDist.add(-dist);
        }

        for (int i = k; i < points.length; i++) {
            double dist = Math.sqrt(points[i][0] * points[i][0] + points[i][1] * points[i][1]);
            kSmallestDist.add(-dist);
            if (!distToPt.containsKey(-dist)) {
                distToPt.put(-dist, new ArrayList<int[]>());
            }
            distToPt.get(-dist).add(points[i]);
            double oldDist = kSmallestDist.remove();
            distToPt.get(oldDist).remove(0);
        }

        int[][] output = new int[k][2];
        int i = 0;

        for (Double d : distToPt.keySet()) {
            for (int[] pt : distToPt.get(d)) {
                output[i] = pt; 
                i++;
            }
        }

        return output;
    }
}
