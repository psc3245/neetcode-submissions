# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = [root]
        answer = []

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.pop(0)
                current_level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            answer.append(current_level)

        return answer
        
        # return self.dfs(root, 0, [])
    def dfs(self, root, depth, levels):
        if root is None:
            return levels
        if root is not None:
            if len(levels) > depth:
                levels[depth].append(root.val)
            else:
                levels.append([root.val])
        if root.left is not None:
            levels = self.dfs(root.left, depth + 1, levels)
        if root.right is not None:
            levels = self.dfs(root.right, depth + 1, levels)
        return levels