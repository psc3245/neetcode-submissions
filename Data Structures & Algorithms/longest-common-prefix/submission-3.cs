public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        string pre = "";
        if (strs[0].Length == 0) return pre;

        while (true) {
            var let = strs[0][pre.Length];
            for (int i = 1; i < strs.Length; i++) {
                if (pre.Length >= strs[i].Length || strs[i][pre.Length] != let) {
                    return pre;
                }
            }
            pre += let;
            if (pre.Length == strs[0].Length) return pre;
        }
        return pre;
    }
}