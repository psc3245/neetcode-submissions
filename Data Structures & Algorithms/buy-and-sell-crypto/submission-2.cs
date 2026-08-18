public class Solution {
    public int MaxProfit(int[] prices) {
        var l = 0;
        var r = 1;
        var maxP = 0;

        while (r < prices.Length) {
            if (prices[l] < prices[r]) {
                var profit = prices[r] - prices[l];
                maxP = Math.Max(profit, maxP);
            }
            else {
                l = r;
            }
            r ++ ;
        }
        return maxP;
    }
}
