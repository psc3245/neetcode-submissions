public class Solution {
    public int LengthOfLongestSubstring(string s) {
        if (s.Length < 2) return s.Length;
        int best = 0;
        int l = 0;
        int r = 1;
        HashSet<char> set = new HashSet<char>();
        set.Add(s[l]);
        while (r < s.Length) {
            if (!set.Contains(s[r])) {
                set.Add(s[r]);
                r += 1;
            }
            else {
                while (set.Contains(s[r])) {
                    set.Remove(s[l]);
                    l += 1;
                }
            }
            best = Math.Max(best, r - l);
        }
        return best;
    }
}
