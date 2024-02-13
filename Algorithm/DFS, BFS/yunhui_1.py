# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        self.dfs(root, '0')
        
        return self.sum 
    
    def dfs(self, node, num : str):
        if node.left == None and node.right == None:
            self.sum += int(num + str(node.val))
            return 
        
        if node.left != None:
            self.dfs(node.left, num+str(node.val))
            
        if node.right != None:
            self.dfs(node.right, num+str(node.val))
