# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, tmp_sum):
            if not node:
                return 0

            tmp = tmp_sum * 10 + node.val
            
            if not node.left and not node.right: # Leaf
                return tmp
            
            return dfs(node.left, tmp) + dfs(node.right, tmp)
        
        return dfs(root, 0)
            
