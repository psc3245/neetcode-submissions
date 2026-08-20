public class Solution {
    public int PivotIndex(int[] nums) {
        List<int> prefix = new List<int>();
        int total = 0;

        for (int i = 0; i < nums.Length; i++) {
            prefix.Add(total);
            total += nums[i];
        }

        List<int> suffix = new List<int>();
        total = 0;

        for (int i = nums.Length - 1; i >= 0; i--) {
            suffix.Add(total);
            total += nums[i];
        }

        suffix.Reverse();

        for (int i = 0; i < nums.Length; i++) {
            if (prefix[i] == suffix[i]) {
                return i;
            }
        }

        return -1;
    }
}