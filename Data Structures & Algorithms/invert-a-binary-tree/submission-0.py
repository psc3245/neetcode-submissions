# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        left_side, right_side = None, None
        if root.left:
            right_side = self.invertTree(root.left)
        if root.right:
            left_side = self.invertTree(root.right)
        root.right = right_side
        root.left = left_side
        return root