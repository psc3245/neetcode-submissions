public class Solution {
    public bool IsPalindrome(string s) {
        int l = 0;
        StringBuilder sb = new StringBuilder();
        foreach (char c in s)
        {
            if (char.IsLetterOrDigit(c))
            {
                sb.Append(char.ToLower(c));
            }
        }
        string newString = sb.ToString();
        int r = newString.Length - 1;
        while (l < r) {
            if (newString[l] != newString[r]) {
                return false;
            }
            l ++;
            r --;
        }
        return true;

    }
}
