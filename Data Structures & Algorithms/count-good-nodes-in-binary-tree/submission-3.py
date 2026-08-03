# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.count(root, root.val)

    def count(self, root, val):
        if not root:
            return 0
        c = 0
        m = val
        if root.val >= val:
            c += 1
            m = root.val
        if root.left:
            c += self.count(root.left, m)
        if root.right:
            c += self.count(root.right, m)

        return c