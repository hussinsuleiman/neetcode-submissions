class Solution {

    public String encode(List<String> strs) {
        StringBuilder s = new StringBuilder();

        for (int i = 0; i < strs.size(); i++) {
            s.append(strs.get(i).length());
            s.append("#");
            s.append(strs.get(i));
        }

        return s.toString();
    }

    public List<String> decode(String str) {
        List<String> strs = new ArrayList<String>();
        int j = 0;
        int i = 0;

        while (i < str.length()) {
            strs.add("");
            int nb = 0;
            
            while (str.charAt(i) != '#') {
                nb = nb*10 + str.charAt(i)-'0';
                i++;
            }

            i++;

            for (int k = 0; k < nb; k++) {
                strs.set(j, strs.get(j) + str.charAt(i+k));
            }

            j++;
            i += nb;
        }
        
        return strs;
    }
}
