class Solution {
    public int timeToEat(int[] piles, int rate) {
        int time = 0;

        for (int i = 0; i < piles.length; i++) {
            time += piles[i] / rate;
            if (piles[i] % rate != 0) {
                time++;
            }
        }

        return time;
    }

    public int minEatingSpeed(int[] piles, int h) {
        int lowerBound = 1;
        int upperBound = 0;
        int mid = 0; 
        int timeTaken = 0;

        for (int i = 0; i < piles.length; i++) {
            upperBound = Math.max(upperBound, piles[i]);
        }

        while (lowerBound < upperBound) {
            mid = (upperBound + lowerBound) / 2;
            timeTaken = timeToEat(piles, mid);

            if (timeTaken <= h) {
                upperBound = mid;
            }
            else {
                lowerBound = mid + 1;
            }
        }
        
        return lowerBound;
    }
}
