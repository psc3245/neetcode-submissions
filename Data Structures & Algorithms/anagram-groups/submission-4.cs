public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        Dictionary<string, int> letterCountToIndex = new Dictionary<string, int>();
        List<List<string>> groups = new List<List<string>>();
        foreach (string s in strs) {
            int[] counts = new int[26];
            foreach (char c in s) {
                var index = c - 'a';
                counts[index] ++;
            }
            var key = string.Join(",", counts);
            if (!letterCountToIndex.ContainsKey(key)) {
                var index = groups.Count;
                List<string> toAdd = new List<string>();
                toAdd.Add(s);
                groups.Add(toAdd);
                letterCountToIndex[key] = index;
            }
            else {
                var index = letterCountToIndex[key];
                groups[index].Add(s);
            }
        }
        return groups;
    }
}
