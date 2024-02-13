# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        num_list = []
        tmp_list = ""
        result = 0

        def dfs(root, tmp):
            if (root is not None):
                tmp += str(root.val)
                if(root.left is None and root.right is None):
                    num_list.append(int(tmp))
                else:
                    dfs(root.left, tmp)
                    dfs(root.right, tmp)

        dfs(root, tmp_list)

        for i in num_list:
            result += i

        return result
