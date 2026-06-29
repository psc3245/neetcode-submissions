/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public static int goodNodes(TreeNode root) {
        int pathMax = root.val;
        int total = 1;
        total += dfs(root.left, pathMax);
        total += dfs(root.right, pathMax);
        return total;
    }

    public static int dfs(TreeNode root, int pathMax) {
        if (root == null) return 0;

        int total = 0;

        if (root.val >= pathMax) {
            total ++;
            pathMax = root.val;
        }

        total += dfs(root.left, pathMax);
        total += dfs(root.right, pathMax);

        return total;

    }
}
