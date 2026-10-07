public class Solution {
    public bool IsPalindrome(string s) {
        var r = s.Length - 1;
        var l = 0;

        while (l < r) {
            if (!char.IsLetterOrDigit(s[l])) {
                l ++;
            }
            else if (!char.IsLetterOrDigit(s[r])) {
                r --;
            }
            else if (char.ToLower(s[r]) != char.ToLower(s[l])) {
                return false;
            }
            else {
                l++;
                r--;
            }
        }
        return true;
    }
}
