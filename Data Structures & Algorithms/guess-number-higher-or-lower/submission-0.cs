/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

public class Solution : GuessGame {
    public int GuessNumber(int n) {
        return GuessNumberHelper(1, n);
    }

    public int GuessNumberHelper(int l, int h) {
        int g = l + (h - l) / 2;

        int result = guess(g);

        if (result == 0) {
            return g;
        }
        else if (result == 1) {
            return GuessNumberHelper(g + 1, h);
        }
        else {
            return GuessNumberHelper(l, g - 1);
        }
    }
}