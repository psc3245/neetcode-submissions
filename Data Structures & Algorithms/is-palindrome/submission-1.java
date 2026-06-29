class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        int left = 0;
        int right = s.length() - 1;

        while (left < right) {
            char lc = s.charAt(left);
            char rc = s.charAt(right);
            boolean lflag = false;
            boolean rflag = false;


            // non alpha numeric (post lower case method)
            if (lc < 48 || ( lc > 57 && lc < 96) ) left++;
            else lflag = true;
            if (rc < 48 || ( rc > 57 && rc < 96) ) right--;
            else rflag = true;

            if (lflag && rflag) {
                if (lc != rc) return false;
                left++;
                right--;
            }

        }

        return true;
    }
}

