class TimeMap {
    HashMap<String, ArrayList<String>> values;
    HashMap<String, ArrayList<Integer>> timeStamps;

    public TimeMap() {
        values = new HashMap<>();
        timeStamps = new HashMap<>();    
    }
    
    public void set(String key, String value, int timestamp) {
        if (values.containsKey(key)) {
            values.get(key).add(value);
            timeStamps.get(key).add(timestamp);
        }
        else {
            ArrayList<String> newValues = new ArrayList<>();
            ArrayList<Integer> newStamps = new ArrayList<>();
            newValues.add(value);
            newStamps.add(timestamp);
            values.put(key, newValues);
            timeStamps.put(key, newStamps);
        }
    }
    
    public String get(String key, int timestamp) {
        if (!values.containsKey(key)) {
            return "";
        }
        
        ArrayList<String> vals = values.get(key);
        ArrayList<Integer> times = timeStamps.get(key);
        
        int start = 0;
        int end = vals.size()-1;
        int mid = 0;

        while (start <= end) {
            mid = (start + end) / 2;

            if (times.get(mid) == timestamp) {
                return vals.get(mid);
            }
            else if (times.get(mid) < timestamp) {
                start = mid + 1; 
            }
            else {
                end = mid - 1;
            }
        }

        if (start < vals.size() && times.get(start) <= timestamp) {
            return vals.get(start);
        }
        if (end >= 0 && times.get(end) <= timestamp) {
            return vals.get(end);
        }
        return "";
    }
}
