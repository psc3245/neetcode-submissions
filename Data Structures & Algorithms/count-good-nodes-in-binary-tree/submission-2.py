# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left = self.goodNodesWithMax(root.left, root.val)
        right = self.goodNodesWithMax(root.right, root.val)
        return left + right + 1

    def goodNodesWithMax(self, root, max):
        path_total = 0
        if root is not None:
            if root.val >= max:
                path_total += 1
                path_max = root.val
            else:
                path_max = max
            path_total += self.goodNodesWithMax(root.left, path_max)
            path_total += self.goodNodesWithMax(root.right, path_max)
        return path_total