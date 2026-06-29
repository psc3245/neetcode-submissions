class Solution {
    public int trap(int[] height) {
        int l = 0;
        int r = height.length - 1;
        int lMax = 0;
        int rMax = 0;
        int total = 0;

        while (l <= r) {
            if (lMax < rMax) {
                if (height[l] <= lMax) {
                    total += Math.min(lMax, rMax) - height[l];
                }
                else {
                    lMax = height[l];
                }

                l++;
            }
            else {
                if (height[r] <= rMax) {
                    total += Math.min(lMax, rMax) - height[r];
                }
                else {
                    rMax = height[r];
                }

                r--;
            }

        }

        return total;
    }
}
