public class Solution {
    public int[] TwoSum(int[] nums, int target) {

        Dictionary<int, int> seen = new Dictionary<int, int>();

        for (int n = 0; n < nums.Length; n++) {
            int complement = target - nums[n];
            if (seen.ContainsKey(complement)) {
                return [seen[complement], n];
            }
            seen[nums[n]] = n;
        }

        return [];

    }
}
