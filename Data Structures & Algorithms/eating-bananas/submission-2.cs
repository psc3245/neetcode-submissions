public class Solution {
    public int MinEatingSpeed(int[] piles, int h) {
        int max = 0;
        foreach (var p in piles) {
            max = Math.Max(max, p);
        }
        if (piles.Length == h) {
            return max;
        }
        return Search(piles, h, 1, max);
    }

    public int Search(int[] piles, int h, int min, int max) {
        if (max == min) return max;
        int rate = (max - min) / 2 + min;
        int time = 0;
        foreach (var p in piles) {
            time += (int)Math.Ceiling((double)p / rate);
        }
        if (time > h) {
            return Search(piles, h, rate + 1, max);
        }
        else {
            return Search(piles, h, min, rate);
        }
    }
}
