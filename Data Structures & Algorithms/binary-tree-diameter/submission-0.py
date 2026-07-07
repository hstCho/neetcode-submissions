# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        # Recursively returns height
        def dfs(curr):
            if not curr:
                return 0

            left = dfs(curr.left)   # height of left of current node
            right = dfs(curr.right) # height of right of current node

            self.res = max(self.res, left + right) # Finding the diameter

            return 1 + max(left, right) # returns height for current node

        dfs(root)
        return self.res