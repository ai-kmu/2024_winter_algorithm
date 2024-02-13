# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    numList = []

    def isLeaf(self, root):
        if root.left is None and root.right is None:
            return True
        else:
            return False

    def dfs(self, root, number):
        if root is not None:
            number += str(root.val)
            if self.isLeaf(root):
                Solution.numList.append(int(number))
            else:
                self.dfs(root.left, number)
                self.dfs(root.right, number)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        Solution.numList = []
        self.dfs(root, "")
        return sum(Solution.numList)
