public class Solution {
    public int FindPeakElement(int[] nums) {
        int highestPeakIndex = 0;
        if (nums.Length < 2) {
            return 0;
        }

        for (int i = 0; i < nums.Length; i++) {
            int right = i + 1;
            int left = i - 1;
            if (i > 0 && i < nums.Length - 1) {
                if (nums[i] > nums[right] && nums[i] > nums[left]) {
                    if (nums[i] > nums[highestPeakIndex]) {
                        highestPeakIndex = i;
                    }
                }
            }
            else if (i == 0) {
                if (nums[i] > nums[right]) {
                    if (nums[i] > nums[highestPeakIndex]) {
                        highestPeakIndex = i;
                    }
                }
            }
            else {
                if (nums[i] > nums[left]) {
                    if (nums[i] > nums[highestPeakIndex]) {
                        highestPeakIndex = i;
                    }
                }
            }
        }

        return highestPeakIndex;
    }
}