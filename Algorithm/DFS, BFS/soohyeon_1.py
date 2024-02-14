# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root):
        def dfs(root, cost):
            if not root.left and not root.right:
                return cost*10 + root.val
            left = dfs(root.left, cost*10+root.val)
            right = dfs(root.right, cost*10+root.val)
            return left + right
        return dfs(root, 0)
