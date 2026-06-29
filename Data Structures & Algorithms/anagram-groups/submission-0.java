class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        
        if (strs.length == 0) return new ArrayList<>();

        if (strs.length == 1) {
            ArrayList<String> temp = new ArrayList<>();
            temp.add(strs[0]);
            List<List<String>> ret = new ArrayList<>();
            ret.add(temp);
            return ret;
        };

        HashMap<String, List<String>> sol = new HashMap<>();

        for (String s : strs) {
            int[] arr = calcArray(s);
            StringBuilder keyBuilder = new StringBuilder();
            for (int count : arr) {
                keyBuilder.append(count).append('#'); // Use '#' as a separator
            }
            String key = keyBuilder.toString();
            sol.putIfAbsent(key, new ArrayList<>());
            sol.get(key).add(s);
        }

        return new ArrayList<>(sol.values());
    }

    public int[] calcArray(String s) {
        int[] arr = new int[26];

        for (int i = 0; i < s.length(); i++) {
            arr[s.charAt(i) - 'a'] ++; // convert to ascii
        }
        return arr;
    }
}
